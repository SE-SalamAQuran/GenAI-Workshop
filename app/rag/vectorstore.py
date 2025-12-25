import chromadb
from chromadb.config import Settings
from app.rag.embeddings import SentenceTransformerEmbeddingFunction

client = chromadb.Client(
    Settings(persist_directory="./chroma_db")
)

embedding_function = SentenceTransformerEmbeddingFunction()

collection = client.get_or_create_collection(
    name="documents",
    embedding_function=embedding_function
)

def add_documents(texts: list[str]):
    collection.add(
        documents=texts,
        ids=[str(i) for i in range(len(texts))]
    )

def query_documents(query: str, n_results=2):
    return collection.query(
        query_texts=[query],
        n_results=n_results
    )
