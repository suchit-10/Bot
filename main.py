import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = "You are SuchitBOT, a witty, smart and slightly sarcastic AI assistant built by Suchit. You are helpful, fun, and always give great answers. Keep responses concise unless asked for detail."

chat_history = []

class Message(BaseModel):
    message: str

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.post("/chat")
def chat(msg: Message):
    chat_history.append({"role": "user", "content": msg.message})

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + chat_history
    )

    reply = response.choices[0].message.content
    chat_history.append({"role": "assistant", "content": reply})

    return {"reply": reply}

@app.delete("/chat")
def clear_chat():
    chat_history.clear()
    return {"status": "cleared"}
