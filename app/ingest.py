import fitz
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

model = SentenceTransformer("all-MiniLM-L6-v2")

def index_pdf(pdf_path, doc_id):

    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()

    chunks = [text[i:i+800] for i in range(0, len(text), 800)]
    embeddings = model.encode(chunks).tolist()

    client = chromadb.Client(Settings(
        chroma_db_impl="duckdb+parquet",
        persist_directory="./chroma_db"
    ))

    collection = client.get_or_create_collection("documents")

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[f"{doc_id}_{i}" for i in range(len(chunks))]
    )

    client.persist()