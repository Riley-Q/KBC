from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json
import random
from backend.question import question_from_llm_by_level

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
pre_questions = []
@app.get("/question/{level}")
def get_question(level: str):
    """
    Fetch one random question from the given level (e.g., '₹1,000').
    """
    print("Level: ", level)
    question = question_from_llm_by_level(level, pre_questions)
    print("pre questions:", pre_questions)
    print(question)
    if question:
        pre_questions.append(question['question'])
    
    return question
