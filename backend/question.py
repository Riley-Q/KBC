import google.generativeai as genai
import os
import json
import random

# configure API key
genai.configure(api_key= "YOUR_API_KEY")
                #os.getenv("GEMINI_API_KEY")

def question_from_llm_by_level(level: str, pre_question: list) -> dict:
    """
    Fetch a question for the given level using Gemini API.
    Returns dict with {question: str, options: list, answer: str}
    """

    prompt = f"""
    You are generating quiz questions for the Indian game show *Kaun Banega Crorepati*.  
    Always return a JSON object with this format:
    {{
    "question": "string",
    "options": ["A: ...", "B: ...", "C: ...", "D: ..."],
    "answer": "A: ..."
    }}

    Previously generated question: {pre_question}

    Rules:
    - Select the question randomly from these categories: 
    General Knowledge (India), Current Affairs, Science & Technology, Culture & Entertainment, Sports, Mythology & Religion, Miscellaneous.
    - Avoid repeating the same category back-to-back more than twice.
    - Keep difficulty aligned with the "level" passed in (higher levels = harder, more niche).
    - Avoid previously generatd questions
    - Always vary the topic for variety.
    - Make sure only ONE option is correct.
    - Use Indian context where relevant.

    """

    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)

    try:
        text = response.text.strip()
        # sometimes Gemini wraps JSON with ```json ... ```
        if text.startswith("```"):
            text = text.split("```")[1]
            text = text.replace("json", "").strip()
        data = json.loads(text)
        return data
    except Exception as e:
        print("Error parsing Gemini response:", e)
        return {
            "question": f"Fallback: What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "answer": "4"
        }

#print(question_from_llm_by_level("₹2,000"))