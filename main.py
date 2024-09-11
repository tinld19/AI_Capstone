import uvicorn
import orjson
from dataclasses import dataclass, field
from fastapi import FastAPI, Request, Response, File, UploadFile
from src.chatbot.search import ChatBot
from src.SeaRoute.sea_route import SeaRoute
# import os

app = FastAPI()

@app.post("/gen-answer")
async def gen_answer(request: Request):
   body = await request.json()
   question = body["question"]
   chatBot = ChatBot()
   response = chatBot.gen_answer(question)
   return {"answer": response}

@app.post("/distance")
async def get_distance(request: Request, response: Response):
   body = await request.body()
   item = orjson.loads(body)
   # get coordinate from
   address_from = item.get("from")
   # get coordinate to
   address_to = item.get("to")
   seaRoute = SeaRoute()
   # print("address_from", address_from)
   # print("address_to", address_to)
   distance, time = seaRoute.compute_distance(address_from, address_to) 
   return {"data": distance, "time": time}

@app.post("/get-location")
async def get_location(request: Request, response: Response):
   body = await request.body()
   item = orjson.loads(body)
   address = item.get("address")
   seaRoute = SeaRoute()      
   location = seaRoute.get_location(address)
   return {"data": location}
   
if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8000)