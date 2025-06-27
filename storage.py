import chromadb
import chromadb

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection("chapters")


def save_version(chapter_id: str, text: str):
    collection.add(documents=[text], ids=[chapter_id])

def retrieve_similar(query: str):
    results = collection.query(query_texts=[query], n_results=3)
    return results["documents"]
