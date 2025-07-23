from pdf2image import convert_from_path
import pytesseract
import tempfile
import os

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# OCR + Embedding
def extract_text_with_ocr(pdf_path):
    with tempfile.TemporaryDirectory() as temp_dir:
        images = convert_from_path(pdf_path, first_page=1, last_page=2)  # Only first 2 pages
        text = ""
        for i, image in enumerate(images):
            image_path = os.path.join(temp_dir, f"page_{i}.png")
            image.save(image_path, "PNG")
            page_text = pytesseract.image_to_string(image)
            text += page_text + "\n\n"
    return text

ocr_text = extract_text_with_ocr("What is ZARI.pdf")
chunks = ocr_text.split("\n\n")[:10]  # Limit to 10 chunks

embedder = SentenceTransformer("paraphrase-MiniLM-L3-v2")
embeddings = embedder.encode(chunks)
index = faiss.IndexFlatL2(embeddings[0].shape[0])
index.add(np.array(embeddings))

def ask_zari(query):
    query_vec = embedder.encode([query])
    _, I = index.search(np.array(query_vec), k=1)
    return chunks[I[0][0]].strip().encode('ascii', 'ignore').decode()
