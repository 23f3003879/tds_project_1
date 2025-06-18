import os
import time
import json
import re
import numpy as np
from pathlib import Path
from tqdm import tqdm
from semantic_text_splitter import MarkdownSplitter
from openai import OpenAI
from dotenv import load_dotenv

# === CONFIG ===
load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://aipipe.org/openai/v1"
)

model_name = "text-embedding-3-small"
folders = ["course_content", "markdowns"]
resume_file = "processed_files.json"
output_file = "embeddings.npz"

# === Rate Limiter ===
class RateLimiter:
    def __init__(self, rpm=60, rps=0.5):
        self.rpm = rpm
        self.rps = rps
        self.last = 0
        self.calls = []

    def wait(self):
        now = time.time()
        if now - self.last < 1 / self.rps:
            time.sleep(1 / self.rps - (now - self.last))
        self.calls = [t for t in self.calls if now - t < 60]
        if len(self.calls) >= self.rpm:
            time.sleep(60 - (now - self.calls[0]))
        self.calls.append(now)
        self.last = time.time()

rate_limiter = RateLimiter()

# === Embedding ===
def get_embedding(text, retries=3):
    for attempt in range(retries):
        try:
            rate_limiter.wait()
            response = client.embeddings.create(
                model=model_name,
                input=text,
                encoding_format="float"
            )
            return response.data[0].embedding
        except Exception as e:
            print(f"[Retry {attempt+1}] Embed failed: {e}")
            time.sleep(2 ** attempt)
    raise RuntimeError("❌ Max retries exceeded")

# === Extract the first post URL from the chunk
POST_URL_PATTERN = re.compile(
    r'https://discourse\.onlinedegree\.iitm\.ac\.in/t/[\w\-]+/\d+/\d+'
)

def extract_first_post_url(text):
    match = POST_URL_PATTERN.search(text)
    return match.group(0) if match else None

# === Chunking with overlap ===
def get_chunks(filepath, size=1500, overlap=250):
    try:
        text = filepath.read_text(encoding="utf-8")
        splitter = MarkdownSplitter(size, overlap)
        return splitter.chunks(text)
    except Exception as e:
        print(f"⚠️ Error reading {filepath.name}: {e}")
        return []

# === Resume support ===
if Path(resume_file).exists():
    processed = set(json.loads(Path(resume_file).read_text()))
else:
    processed = set()

all_chunks = []
all_embeddings = []
all_metadata = []

# === Collect files ===
files = [f for folder in folders for f in Path(folder).rglob("*.md")]
files_to_process = [f for f in files if str(f) not in processed]
print(f"📁 Found {len(files_to_process)} new markdown files to embed.")

# === Main embedding loop ===
with tqdm(total=len(files_to_process), desc="📦 Embedding files") as pbar:
    for file in files_to_process:
        chunks = get_chunks(file)
        for chunk in chunks:
            try:
                emb = get_embedding(chunk)
                chunk_urls = POST_URL_PATTERN.findall(chunk)

                all_chunks.append(chunk)
                all_embeddings.append(emb)
                all_metadata.append({
                    "file": str(file),
                    "preview": chunk[:100],
                    "urls": list(set(chunk_urls))
                })
            except Exception as e:
                print(f"⚠️ Skipped chunk from {file.name}: {e}")
        processed.add(str(file))
        with open(resume_file, "w", encoding="utf-8") as f:
            json.dump(list(processed), f, indent=2)
        pbar.update(1)

# === Save embeddings ===
if all_chunks:
    np.savez_compressed(
        output_file,
        chunks=np.array(all_chunks, dtype=object),
        embeddings=np.array(all_embeddings, dtype=np.float32),
        metadata=np.array(all_metadata, dtype=object)
    )
    print(f"✅ Saved {len(all_chunks)} embeddings to `{output_file}`")
else:
    print("⚠️ No new embeddings were generated.")