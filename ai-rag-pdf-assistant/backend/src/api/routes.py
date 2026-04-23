from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import shutil

from src.services.rag_service import RAGService

router = APIRouter()
rag = RAGService()

class Query(BaseModel):
    query: str

@router.get("/")
def read_root():
    return {"message": "Backend API is working"}

@router.post("/upload-pdf")
def upload(file: UploadFile = File(...)):
    path = f"temp_{file.filename}"
    with open(path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    rag.ingest_pdf(path)
    return {"msg": "PDF processed"}

@router.post("/query")
def query(q: Query):
    return {"response": rag.process(q.query)}