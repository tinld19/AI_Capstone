import os
import uvicorn
import orjson

from dataclasses import dataclass, field
from fastapi import FastAPI, Request, Response, HTTPException
from typing import List

from src.chatbot.search import ChatBot
from src.SeaRoute.sea_route import SeaRoute
from src.OCR.mainOCR import OCRDoc
from src.vision.main_vision import VisionServices
from src.AWS_S3.file_helper import S3Helper

app = FastAPI()


@app.post("/gen-answer")
async def gen_answer_chat(request: Request):
   try:
      body = await request.json()
      question = body["question"]
      chatBot = ChatBot()
      response, rl = chatBot.gen_answer(question)
      return {"answer": response, "domain": rl}
   except Exception as e:
      raise HTTPException(status_code=500, detail=f"Error generating answer: {str(e)}")

@app.post("/distance")
async def get_distance(request: Request, response: Response):
   try:
      body = await request.body()
      item = orjson.loads(body)
      address_from = item.get("from")
      address_to = item.get("to")
      seaRoute = SeaRoute()
      distance, time = seaRoute.compute_distance(address_from, address_to) 
      return {"data": distance, "time": time}
   except Exception as e:
      raise HTTPException(status_code=500, detail=f"Error calculating distance: {str(e)}")

@app.post("/get-location")
async def get_location(request: Request, response: Response):
   try:
      body = await request.body()
      item = orjson.loads(body)
      address = item.get("address")
      seaRoute = SeaRoute()      
      location = seaRoute.get_location(address)
      return {"data": location}
   except Exception as e:
      raise HTTPException(status_code=500, detail=f"Error find location: {str(e)}")

@app.post("/extract-ocr")
async def extract_ocr(request: Request):
   try:
      body = await request.body()
      item = orjson.loads(body)
      bucket_name = item.get("bucket_name")
      path_file = item.get("s3_file")
      s3Helper = S3Helper()
      ocrDoc = OCRDoc()
      tmp_pdf_dir = "./tmp_pdf"
      if not os.path.exists(tmp_pdf_dir):
         os.makedirs(tmp_pdf_dir)
      path_local = os.path.join(tmp_pdf_dir, path_file.split("/")[-1])
      path_local = s3Helper.download_pdf_from_s3(bucket_name, path_file, path_local)
      json_extract = ocrDoc.data_extract(path_local)
      return {"data": json_extract}
   except Exception as e:
      raise HTTPException(status_code=500, detail=f"Error extracting OCR: {str(e)}")

@app.post("/damaged-detect")
async def damaged_detect(request: Request):
   try:
      
      body = await request.body()
      item = orjson.loads(body)
      bucket_name = item.get("bucket_name")
      path_files = item.get("s3_files")

      s3Helper = S3Helper()
      visionServices = VisionServices()
      total_res = []

      for file in path_files:
         number_of_detections = {}
         image = s3Helper.read_image_from_s3(bucket_name, file)
         number_of_damaged, res_proportion, output_path, image_inference = visionServices.detection_damage(file, image)
         number_of_detections["file image"] = output_path
         number_of_detections["number of damage"] = len(number_of_damaged)
         number_of_detections["rate error"] = res_proportion
         upload_img = s3Helper.upload_image_to_s3(image_inference, bucket_name, output_path)
         total_res.append(number_of_detections)
      return {"detections": total_res}
   except Exception as e:
      raise HTTPException(status_code=500, detail=f"Error detecting damage: {str(e)}")

# @app.get("/load-data-chat")
# async def load_data_chat(request: Request, response: Response):
#    try:
#       chatBot = ChatBot()
#       chatBot.load_data()
#       return {"status": "load success"}
#    except Exception as e:
#       raise HTTPException(status_code=500, detail=f"Error loading chat data: {str(e)}")
   
if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8000, workers = 1)