from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
from .llm import generate_answer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client(Settings(
    chroma_db_impl="duckdb+parquet",
    persist_directory="./chroma_db"
))

collection = client.get_or_create_collection("documents")

def ask(question):

    query_embedding = model.encode([question]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=5
    )

    context = "\n\n".join(results["documents"][0])

    prompt = f"""
    Use o contexto abaixo para responder a pergunta.
    Se não souber, diga que não sabe.

    Contexto:
    {context}

    Pergunta:
    {question}
    """

    return generate_answer(prompt)