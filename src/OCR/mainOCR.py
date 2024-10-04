from .models.paddle_model import OCRProcessor
import json
import sys
import os
from .models.llm_ocr import LLM_OCR

class OCRDoc:
   
   @staticmethod
   def gen_data(data_text):
      llm_ocr = LLM_OCR()
      extract_data = llm_ocr.extract_data_ocr(data_text)
      return extract_data
   
   @staticmethod
   def data_extract(path_file):
      ocr_processor = OCRProcessor()
      result_data = ocr_processor.predict_OCR(path_file)
      json_extract = OCRDoc.gen_data(result_data)
      # data_json = json.loads(json_extract)
      return json_extract