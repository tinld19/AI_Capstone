import uvicorn
from dataclasses import dataclass, field
from fastapi import FastAPI, Request, Response, File, UploadFile
from src.chatbot.search import ChatBot
# import os

app = FastAPI()

@app.post("/gen-answer")
async def gen_answer(request: Request):
   body = await request.json()
   question = body["question"]
   chatBot = ChatBot()
   response = chatBot.gen_answer(question)
   return {"answer": response}

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8000)