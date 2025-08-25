# 🎮 KBC Game  

A web-based version of *Kaun Banega Crorepati* built with **HTML, CSS, JS** (frontend) and **FastAPI + Gemini LLM** (backend).  

## ✨ Features  
- Dynamic questions from Gemini LLM  
- Prize ladder with highlights  
- Lifelines: 50:50, Phone a Friend, Audience Poll  
- Camera feed + game sounds  
- Correct/wrong answers highlighted (green/red)  
- Avoids repeating questions in same session  

## 🚀 Setup  
1. Clone repo & install deps:  
   ```bash
   pip install fastapi uvicorn google-generativeai
   
2. Add your Gemini API key in .env:
   ```bash
   GEMINI_API_KEY=your_api_key_here
   
4. Run backend:
   ```bash
   uvicorn backend.app:app --reload

### 🎯 How to Play

- Answer questions & climb the money ladder
- Use lifelines wisely
- Wrong answer → Game Over
