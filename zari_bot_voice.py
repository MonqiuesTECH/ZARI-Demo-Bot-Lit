import pdfplumber
import os
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = "\n\n".join(page.extract_text() or "" for page in pdf.pages)
    return text

# Chunking helper (simple newline-based for now)
def chunk_text(text, max_chunks=10):
    raw_chunks = text.strip().split("\n\n")
    return raw_chunks[:max_chunks]

# Load model once
embedder = SentenceTransformer("paraphrase-MiniLM-L3-v2")

# Prepare embeddings (only on startup)
document_text = extract_text_from_pdf("What is ZARI.pdf")
chunks = chunk_text(document_text)

embeddings = embedder.encode(chunks)
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# Query logic
def ask_zari(query):
    query_vec = embedder.encode([query])
    D, I = index.search(np.array(query_vec), k=1)
    score = D[0][0]

    if score > 2.0:  # Adjustable threshold — lower = stricter
        return "I'm not confident in my answer. Can you rephrase that?"

    return chunks[I[0][0]]
