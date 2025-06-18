import os
import time
import json
import base64
import numpy as np
import re
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai

# === ENV & Clients ===
load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://aipipe.org/openai/v1"
)
genai.configure(api_key=os.getenv("GENAI_API_KEY"))

EMBED_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4o-mini"
VISION_MODEL = "gpt-4o"

# === App & Data ===
app = FastAPI()
chunks, embeddings = None, None

import os

def load_embeddings():
    global chunks, embeddings
    embeddings_path = os.path.join(os.path.dirname(__file__), "embeddings.npz")
    data = np.load(embeddings_path, allow_pickle=True)
    chunks = data["chunks"]
    embeddings = data["embeddings"]
    print(f"✅ Loaded {len(chunks)} chunks")

load_embeddings()

# === Pydantic Schema ===
class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None

# === Shared Rate Limiter ===
class RateLimiter:
    def __init__(self, rpm=60, rps=1):
        self.rpm = rpm
        self.rps = rps
        self.last = 0
        self.calls = []

    def wait(self):
        now = time.time()
        self.calls = [t for t in self.calls if now - t < 60]
        if len(self.calls) >= self.rpm:
            time.sleep(60 - (now - self.calls[0]))
        if now - self.last < 1 / self.rps:
            time.sleep((1 / self.rps) - (now - self.last))
        self.calls.append(time.time())
        self.last = time.time()

rate_limiter = RateLimiter()

# === Embedding ===
def get_embedding(text, retries=3):
    for attempt in range(retries):
        try:
            rate_limiter.wait()
            res = client.embeddings.create(
                model=EMBED_MODEL,
                input=text,
                encoding_format="float"
            )
            return res.data[0].embedding
        except Exception as e:
            print(f"[Retry {attempt+1}] Embedding failed: {e}")
            time.sleep(2 ** attempt)
    raise RuntimeError("❌ Embedding failed after retries")

# === Image Caption ===
def get_image_caption(image_b64: str) -> str:
    try:
        rate_limiter.wait()
        model = genai.GenerativeModel(VISION_MODEL)
        image_data = {
            "mime_type": "image/jpeg",
            "data": base64.b64decode(image_b64)
        }
        response = model.generate_content([
            image_data,
            "Describe this image briefly in one sentence."
        ])
        return response.text.strip()
    except Exception as e:
        print(f"[Image Caption Error] {e}")
        return ""

# === LLM Generation ===
def generate_llm_response(question: str, context: str) -> str:
    try:
        rate_limiter.wait()
        system_prompt = """You are a helpful and responsible teaching assistant.
Your job is to answer student questions strictly based on the provided context.

Guidelines:
- If the context does not contain sufficient information to answer the question, reply exactly with: `I don't know`.
- Do not fabricate information or make assumptions beyond what is explicitly mentioned in the context.
- Format your response using proper Markdown, including:
  - Headings (`##`) if needed
  - Bullet points for clarity
  - Code blocks using triple backticks (```) for any code or commands
  - Links should be clearly labeled if referenced

Important:
- Keep your answer factual, concise, and neutral in tone.
- Never include disclaimers, system messages, or references to yourself (e.g., "As an AI language model...").
- Do not refer to the context itself (e.g., "Based on the context above..."). Just answer naturally.
"""
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
        ]
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages=messages,
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error during LLM generation: {e}"

# === Helper: Extract URL + Snippet ===
def extract_url_and_snippet(chunk):
    match = re.search(r'https?://[^\s)>\]]+', chunk)
    url = match.group(0) if match else "No URL"
    first_line = chunk.strip().split("\n")[0]
    snippet = first_line[:150]
    return {"url": url, "text": snippet}

# === RAG Retrieval + Generation ===
def answer(question: str, image: Optional[str] = None):
    if image:
        caption = get_image_caption(image)
        question += f"\n\nImage Context: {caption}"

    question_emb = get_embedding(question)
    similarities = np.dot(embeddings, question_emb) / (
        np.linalg.norm(embeddings, axis=1) * np.linalg.norm(question_emb)
    )
    top_indices = np.argsort(similarities)[-10:][::-1]
    top_chunks = [chunks[i] for i in top_indices]

    context = "\n\n".join(top_chunks)
    response = generate_llm_response(question, context)

    # ✅ If the model doesn't know, return empty sources
    if response.strip().lower() == "i don't know.":
        sources = []
    else:
        sources = [extract_url_and_snippet(chunk) for chunk in top_chunks]

    return {
        "question": question,
        "answer": response,
        "sources": sources
    }

# === Routes ===
@app.post("/api/query")
async def query(request: QuestionRequest):
    try:
        return answer(request.question, request.image)
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
async def root():
    return {"message": "RAG API is running!"}
