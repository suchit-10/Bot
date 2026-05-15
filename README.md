# 🤖 BOT

A crazy dark-themed AI chatbot built with FastAPI + Groq (Llama 3.3 70B) + Three.js 3D animations.
<img width="869" height="631" alt="image" src="https://github.com/user-attachments/assets/f6a6297f-01e4-44ec-b963-e328a43efef7" />




## Features
- 🌌 3D galaxy particle background
- 💎 Glassmorphism dark UI
- ⚡ Powered by Llama 3.3 70B via Groq (free & fast)
- 🎨 Neon animations with GSAP & Three.js
- 📝 Markdown + syntax highlighted code blocks

## Setup

1. Clone the repo
   ```bash
   git clone https://github.com/<your-username>/SuchitBOT.git
   cd SuchitBOT
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Create `.env` file
   ```
   GROQ_API_KEY=your_groq_api_key
   ```

4. Run
   ```bash
   python -m uvicorn main:app --reload
   ```

5. Open `http://localhost:8000`

## Get Free Groq API Key
👉 [console.groq.com](https://console.groq.com)
