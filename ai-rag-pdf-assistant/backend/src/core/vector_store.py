import faiss
import numpy as np

class VectorStore:
    def __init__(self):
        self.index = faiss.IndexFlatL2(384)
        self.docs = []

    def add(self, embeddings, docs):
        self.index.add(np.array(embeddings).astype("float32"))
        self.docs.extend(docs)

    def search(self, emb, k=3):
        D, I = self.index.search(np.array([emb]).astype("float32"), k)
        return [self.docs[i] for i in I[0]]