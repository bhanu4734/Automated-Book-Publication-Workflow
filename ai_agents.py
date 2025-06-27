import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")
def spin_chapter(text: str) -> str:
    prompt = f"Rewrite this book chapter in a more polished literary style:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.strip()
def review_chapter(text: str) -> str:
    prompt = f"Please review and suggest improvements for this rewritten chapter:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.strip()
