from paddleocr import PaddleOCR
import numpy as np
import matplotlib.pyplot as plt
import fitz
import os
import cv2

class OCRProcessor:
   def __init__(self, use_angle_cls=True, use_gpu=True):
      self.ocr = PaddleOCR(use_angle_cls=use_angle_cls, use_gpu=use_gpu)
   
   def convert_pdf_to_images(self, pdf_path, output_base_dir="images", zoom=4):
      pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
      output_dir = os.path.join(output_base_dir, pdf_name)
    
      if not os.path.exists(output_dir):
         os.makedirs(output_dir)
         
      image_paths = []
      doc = fitz.open(pdf_path)
      mat = fitz.Matrix(zoom, zoom)
      
      for i in range(len(doc)):
         page = doc.load_page(i)
         pix = page.get_pixmap(matrix=mat)
         image_path = os.path.join(output_dir, f"image_{i+1}.png")
         pix.save(image_path)
         image_paths.append(image_path)
      doc.close()
      return image_paths

   def predict_OCR(self, file_path):
      if file_path.lower().endswith('.pdf'):
         image_paths = self.convert_pdf_to_images(file_path)
      else:
         image_paths = [file_path]
      for img_path in image_paths:
         result = self.ocr.ocr(img_path)
         list_text = []
         for res in result:
               for line in res:
                  text = line[1][0]
                  list_text.append(text)
         data = "\n".join(list_text)
         return data
      
# if __name__ == "__main__":
#    ocr_processor = OCRProcessor()
#    path_file = "/root/AI_Capstone/src/OCR/files/to-khai-hai-quan-xk_2805201309.pdf"
#    result_data = ocr_processor.predict_OCR(path_file)
#    print(result_data)
