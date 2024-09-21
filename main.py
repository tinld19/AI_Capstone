import uvicorn
import orjson
from dataclasses import dataclass, field
from fastapi import FastAPI, Request, Response, File, UploadFile
from src.chatbot.search import ChatBot
from src.SeaRoute.sea_route import SeaRoute
from src.OCR.mainOCR import OCRDoc

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
   address_from = item.get("from")
   address_to = item.get("to")
   seaRoute = SeaRoute()
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

@app.post("/extract-ocr")
async def extract_ocr(request: Request, response: Response):
   body = await request.body()
   item = orjson.loads(body)
   path_file = item.get("path_file")
   ocrDoc = OCRDoc()
   json_extract = ocrDoc.data_extract(path_file)
   return {"data": json_extract}

@app.get("/load-data-chat")
async def load_data_chat(request: Request, response: Response):
   chatBot = ChatBot()
   chatBot.load_data()
   return {"status": "load success"}
   
if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8000, workers = 1)