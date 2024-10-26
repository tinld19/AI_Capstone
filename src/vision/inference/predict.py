import os
import uuid
from PIL import Image
import matplotlib.pyplot as plt
from ultralytics import YOLO
import cv2

model_path = 'src/vision/weights/container_detection_ver1_1.pt'

class DamageDetector:
   def __init__(self):
      self.model_path = model_path
      self.model = YOLO(model_path)

   def predict(self, file, image_paths):
      results = self.model(image_paths)
      number_of_damaged = results[0].boxes.cls.tolist()

      for idx, result in enumerate(results):
         img_with_boxes = result.plot()
         img_rgb = cv2.cvtColor(img_with_boxes, cv2.COLOR_BGR2RGB) 
         random_id = str(uuid.uuid4())
         img = Image.fromarray(img_rgb)
         output_path = os.path.join(f"inference_detect/{file.split(".")[0].split("/")[-1]}_{idx}_{random_id}.jpeg")
               
      res_proportion = self.calculate_bounding_box_areas(results)
      
      return number_of_damaged, res_proportion, output_path, img

   def calculate_bounding_box_areas(self, results):
      areas = []
      for result in results:
         boxes = result.boxes.xyxy.tolist()
         for box in boxes:
               x_min, y_min, x_max, y_max = box[:4]
               width = x_max - x_min
               height = y_max - y_min
               area = width * height
               if area <= 10000:
                  proportion = 10
               elif area <= 30000:
                  proportion = 30
               elif area <= 60000:
                  proportion = 60
               elif area <= 90000:
                  proportion = 70
               elif area <= 120000:
                  proportion = 80
               else:
                  proportion = 100
               areas.append(proportion)
      res_proportion = sum(areas)/(len(areas) + 0.1)
      if res_proportion >= 100:
         res_proportion = 100
      return res_proportion