from src.core.vector_store import VectorStore
from src.core.embeddings import EmbeddingModel

class Retriever:
    def __init__(self):
        self.store = VectorStore()
        self.embedder = EmbeddingModel()

    def add_documents(self, docs):
        emb = self.embedder.encode(docs)
        self.store.add(emb, docs)

    def retrieve(self, query):
        q_emb = self.embedder.encode([query])[0]
        docs = self.store.search(q_emb)
        return " ".join(docs)