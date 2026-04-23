# AI RAG PDF Assistant (Gemini + FastAPI + React)

A full-stack AI application that allows users to upload PDFs and ask questions using Retrieval-Augmented Generation (RAG) powered by Google Gemini.

---

##  Features

*  Upload PDF documents
*  Semantic search using FAISS
*  Real embeddings (Sentence Transformers)
*  Gemini-powered answers
*  FastAPI backend
*  Chat-style React frontend

---

## Tech Stack

* **Frontend:** React (Vite), Axios
* **Backend:** FastAPI
* **LLM:** Google Gemini
* **Vector DB:** FAISS
* **Embeddings:** Sentence Transformers

---

## 📁 Project Structure

```
backend/
  src/
  main.py
  requirements.txt

frontend/
  src/
  public/
  package.json
  vite.config.js
```

---

## ⚙️ Setup Instructions

### 🔹 Backend Setup

```bash
cd backend
pip3 install -r requirements.txt
python -m uvicorn main:app --reload
```

 Create a `.env` file inside backend:

```
GEMINI_API_KEY=your_api_key_here
MODEL_NAME=gemini-1.5-flash
```

---

### 🔹 Frontend Setup

```bash
cd frontend
npm install
npm install axios
npm audit fix
npm run dev
```

---

##  Usage

1. Upload a PDF
2. Ask questions in chat
3. Get AI-generated answers based on document context

---

##  Example

**Input:**
What is machine learning?

**Output:**
Machine learning is a subset of AI that learns from data.

---

## 📌 Future Improvements

* Chat history
* Multi-document support
* Authentication system
* Deployment (Render / Netlify)

---

##  Author

Avinash
