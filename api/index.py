import os
import time
import json
import base64
import numpy as np
import re
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
from openai import OpenAI
from app.main import app as handler


# === Load environment ===
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://aipipe.org/openai/v1"
)

EMBED_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4o-mini"

# === App & Data ===
app = FastAPI()

chunks, embeddings = None, None
def load_embeddings():
    global chunks, embeddings
    embeddings_path = os.path.join(os.path.dirname(__file__), "embeddings.npz")
    data = np.load(embeddings_path, allow_pickle=True)
    chunks = data["chunks"]
    embeddings = data["embeddings"]
load_embeddings()

# === Request Schema ===
class QuestionRequest(BaseModel):
    question: str
    image: Optional[str] = None  # Ignored for now in serverless mode

# === Rate limiter ===
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
def get_embedding(text):
    rate_limiter.wait()
    res = client.embeddings.create(
        model=EMBED_MODEL,
        input=text,
        encoding_format="float"
    )
    return res.data[0].embedding

# === LLM Response ===
def generate_llm_response(question: str, context: str):
    system_prompt = """You are a helpful and responsible teaching assistant.
Answer the question strictly based on the context. Use markdown.
If the answer is not in the context, respond with: `I don't know`.
"""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
    ]
    rate_limiter.wait()
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=messages,
        temperature=0.3
    )
    return response.choices[0].message.content

# === Extract snippet & link ===
def extract_url_and_snippet(chunk):
    match = re.search(r'https?://[^\s)>\]]+', chunk)
    url = match.group(0) if match else "No URL"
    first_line = chunk.strip().split("\n")[0]
    snippet = first_line[:150]
    return {"url": url, "text": snippet}

# === Core logic ===
def answer(question: str):
    question_emb = get_embedding(question)
    similarities = np.dot(embeddings, question_emb) / (
        np.linalg.norm(embeddings, axis=1) * np.linalg.norm(question_emb)
    )
    top_indices = np.argsort(similarities)[-10:][::-1]
    top_chunks = [chunks[i] for i in top_indices]
    context = "\n\n".join(top_chunks)
    response = generate_llm_response(question, context)
    return {
        "question": question,
        "answer": response,
        "sources": [extract_url_and_snippet(c) for c in top_chunks]
    }

# === Route ===
@app.post("/api/query")
async def query(request: Request):
    data = await request.json()
    question = data.get("question", "")
    return answer(question)

@app.get("/")
async def root():
    return {"message": "Virtual TA API is live!"}
