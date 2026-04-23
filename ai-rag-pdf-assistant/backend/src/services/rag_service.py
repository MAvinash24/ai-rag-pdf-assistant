from src.core.retriever import Retriever
from src.core.llm_engine import LLMEngine
from src.core.pdf_loader import PDFLoader, chunk_text

class RAGService:
    def __init__(self):
        self.ret = Retriever()
        self.llm = LLMEngine()
        self.loader = PDFLoader()

    def ingest_pdf(self, path):
        text = self.loader.load(path)
        chunks = chunk_text(text)
        self.ret.add_documents(chunks)

    def process(self, query):
        context = self.ret.retrieve(query)
        return self.llm.generate(query, context)