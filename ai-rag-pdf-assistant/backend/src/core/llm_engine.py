import google.generativeai as genai
from src.utils.config import GEMINI_API_KEY, MODEL_NAME

genai.configure(api_key=GEMINI_API_KEY)

class LLMEngine:
    def __init__(self):
        self.model = genai.GenerativeModel(MODEL_NAME)

    def generate(self, query, context):
        prompt = f"""
Context:
{context}

Question:
{query}

Answer clearly and concisely.
"""
        res = self.model.generate_content(prompt)
        return res.text if res.text else "No response"