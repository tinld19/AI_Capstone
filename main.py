import uvicorn
import orjson
from dataclasses import dataclass, field
from fastapi import FastAPI, Request, Response, File, UploadFile
from typing import List
from src.chatbot.search import ChatBot
from src.SeaRoute.sea_route import SeaRoute
from src.OCR.mainOCR import OCRDoc
from src.vision.main_vision import VisionServices
import os

app = FastAPI()

@app.post("/gen-answer")
async def gen_answer(request: Request):
   body = await request.json()
   question = body["question"]
   chatBot = ChatBot()
   response, rl = chatBot.gen_answer(question)
   return {"answer": response, "domain": rl}

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
async def extract_ocr(file: UploadFile = File(...)):
   upload_folder = "/tmp_pdf"

   if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
        
   contents = await file.read()
   path_file = f"/tmp_pdf/{file.filename}"
   with open(path_file, "wb") as f:
      f.write(contents)
   ocrDoc = OCRDoc()
   json_extract = ocrDoc.data_extract(path_file)
   return {"data": json_extract}

@app.post("/damaged-detect")
async def damaged_detect(files: List[UploadFile] = File(...)):
   upload_folder = "/tmp_images"
   if not os.path.exists(upload_folder):
      os.makedirs(upload_folder)

   total_res = []

   for file in files:
      number_of_detections = {}
      contents = await file.read()
      path_file = os.path.join(upload_folder, file.filename)
      with open(path_file, "wb") as f:
         f.write(contents)
      visionServices = VisionServices()
      number_of_damaged, res_proportion, output_path = visionServices.detection_damage(path_file)
      number_of_detections["file image"] = output_path
      number_of_detections["number of damage"] = len(number_of_damaged)
      number_of_detections["rate error"] = res_proportion
      total_res.append(number_of_detections)
   return {"detections": total_res}

@app.get("/load-data-chat")
async def load_data_chat(request: Request, response: Response):
   chatBot = ChatBot()
   chatBot.load_data()
   return {"status": "load success"}
   
if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8000, workers = 1)