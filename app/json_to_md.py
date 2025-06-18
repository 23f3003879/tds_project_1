import os
import json
import re
import time
import tempfile
import requests
from pathlib import Path
from PIL import Image
from bs4 import BeautifulSoup
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai
import random

# === Config ===
load_dotenv()
genai.api_key = os.getenv("GOOGLE_API_KEY")
model = genai.GenerativeModel("gemini-2.0-flash")

INPUT_DIR = "discourse_json"
OUTPUT_DIR = os.path.join("markdowns", "discourse")
ALLOWED_DOMAIN = "europe1.discourse-cdn"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# === Helpers ===
def sanitize_slug(slug):
    return re.sub(r'[^\w\-]', '_', slug.strip().lower())

def html_to_markdown(html):
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style"]): tag.decompose()
    for br in soup.find_all("br"): br.replace_with("\n")
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if src.lower().endswith(".gif"):  # Skip gifs
            img.decompose()
            continue
        alt = img.get("alt", "image")
        img.replace_with(f"![{alt}]({src})")
    for a in soup.find_all("a"):
        href = a.get("href", "#")
        text = a.get_text(strip=True)
        a.replace_with(f"[{text}]({href})")
    markdown = soup.get_text(separator="\n").strip()
    markdown = re.sub(r'[ \t]+$', '', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'\n{2,}', '\n\n', markdown)
    return markdown

def download_image(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as f:
            f.write(response.content)
            return f.name
    except Exception as e:
        print(f"[ERROR] Download failed: {url} — {e}")
        return None

def generate_caption(image_path, max_retries=5):
    delay = 2  # start with 2 seconds
    for attempt in range(1, max_retries + 1):
        try:
            with Image.open(image_path) as img:
                response = model.generate_content([
                    img,
                    "Describe this image concisely and factually for a student in the Tools in Data Science course."
                    "Focus on visible content like code, graphs, tables. No greetings or assumptions."
                ])
                # Optional delay between successful requests to reduce request rate
                time.sleep(6)
                return response.text.strip()
        except Exception as e:
            if "429" in str(e) or "rate" in str(e).lower():
                print(f"[RATE LIMIT] Attempt {attempt}/{max_retries} — Retrying in {delay:.1f}s...")
                time.sleep(delay + random.uniform(0.1, 0.5))  # jitter
                delay *= 2  # exponential backoff
            else:
                print(f"[ERROR] Caption gen failed for {image_path}: {e}")
                break
    print(f"[FAILED] Gave up on caption after {max_retries} retries: {image_path}")
    return None

def should_process(url):
    return ALLOWED_DOMAIN in url and not url.lower().endswith(".gif")

def update_image_descriptions(md_path):
    text = Path(md_path).read_text(encoding="utf-8")
    INLINE_IMG_PATTERN = re.compile(r'!\[([^\]]*)\]\((https?://[^\)]+)\)')
    already_has_desc = re.compile(r'\n> \*\*Image Description\*\*:', re.IGNORECASE)
    modified = False

    def add_description(match):
        alt, url = match.groups()
        if not should_process(url):
            return match.group(0)

        if f"{url})\n\n> **Image Description**:" in text:
            return match.group(0)

        print(f"[IMG] Captioning missing: {url}")
        path = download_image(url)
        if not path:
            return match.group(0)
        caption = generate_caption(path)
        os.remove(path)
        if not caption:
            return match.group(0)

        nonlocal modified
        modified = True
        return f"![{alt}]({url})\n\n> **Image Description**: {caption}\n"

    updated = INLINE_IMG_PATTERN.sub(add_description, text)
    if modified:
        backup_path = Path(md_path).with_suffix(".backup.md")
        Path(md_path).rename(backup_path)
        Path(md_path).write_text(updated, encoding="utf-8")
        print(f"[✓] Updated captions in {Path(md_path).name}")
    else:
        print(f"[✔] No update needed: {Path(md_path).name}")

def process_topic_json(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    topic_id = data.get("id")
    topic_slug = sanitize_slug(data.get("slug", f"topic_{topic_id}"))
    topic_title = data.get("title", "Untitled Topic").strip()
    posts = data.get("post_stream", {}).get("posts", [])

    if not topic_id or not posts:
        print(f"⏭️ Skipping {filepath} — no posts or ID.")
        return

    filename = f"topic_{topic_id}_{topic_slug}.md"
    output_path = Path(OUTPUT_DIR) / filename

    if output_path.exists():
        print(f"[~] Markdown exists: {filename}. Checking captions...")
        update_image_descriptions(output_path)
        return

    print(f"[+] Creating markdown for: {filename}")
    lines = [
        f"---",
        f"title: \"{topic_title}\"",
        f"topic_id: {topic_id}",
        f"slug: \"{topic_slug}\"",
        f"original_url: https://discourse.onlinedegree.iitm.ac.in/t/{topic_slug}/{topic_id}",
        f"downloaded_at: \"{datetime.now().isoformat()}\"",
        f"---\n"
    ]

    for post in sorted(posts, key=lambda x: x.get("post_number", 0)):
        author = post.get("display_username", post.get("username", "unknown user"))
        created_at = post.get("created_at", "")
        cooked = post.get("cooked", "")
        content_md = html_to_markdown(cooked)
        url = post.get("absolute_post_url")
        lines.append(f"### Post #{post.get('post_number')} by {author} on {created_at}")
        if url:
            lines.append(f"**Post URL**: {url}\n")
        lines.append(content_md)
        lines.append("\n---\n")

    md_text = "\n".join(lines)
    cleaned, _ = process_markdown_content(md_text)  # Optionally caption at creation
    output_path.write_text(cleaned, encoding="utf-8")
    print(f"✅ Created: {filename}")

def process_markdown_content(md_text):
    INLINE_IMG_PATTERN = re.compile(r'!\[([^\]]*)\]\((https?://[^\)]+)\)')
    modified = False
    seen = set()

    def process_img(match):
        alt, url = match.groups()
        if not should_process(url) or url in seen:
            return match.group(0)
        seen.add(url)
        print(f"[IMG] Processing new: {url}")
        path = download_image(url)
        if not path:
            return match.group(0)
        caption = generate_caption(path)
        os.remove(path)
        if not caption:
            return match.group(0)
        nonlocal modified
        modified = True
        return f"![{alt}]({url})\n\n> **Image Description**: {caption}\n"

    updated = INLINE_IMG_PATTERN.sub(process_img, md_text)
    updated = re.sub(r'\n{3,}', '\n\n', updated)
    return updated, modified

def main():
    json_files = sorted(Path(INPUT_DIR).glob("*.json"))
    print(f"🧩 Found {len(json_files)} JSON topics.")
    for file in json_files:
        try:
            process_topic_json(file)
        except Exception as e:
            print(f"[ERROR] Failed: {file.name} — {e}")
    print("🎉 Done!")

if __name__ == "__main__":
    main()
