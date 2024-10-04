import os
import uuid
from PIL import Image
import matplotlib.pyplot as plt
from ultralytics import YOLO

model_path = 'src/vision/weights/container_detection_ver1_1.pt'

class DamageDetector:
   def __init__(self, save_dir='src/vision/image'):
      self.model_path = model_path
      self.save_dir = save_dir
      self.model = YOLO(model_path)

      if not os.path.exists(self.save_dir):
         os.makedirs(self.save_dir)

   def predict(self, image_paths):
      results = self.model(image_paths)
      number_of_damaged = results[0].boxes.cls.tolist()

      for idx, result in enumerate(results):
         img_with_boxes = result.plot()
         random_id = str(uuid.uuid4())
         img = Image.fromarray(img_with_boxes)
         output_path = os.path.join(self.save_dir, f"output_image_{idx}_{random_id}.jpg")
         img.save(output_path)
         print(f"Image saved at: {output_path}")
         
      res_proportion = self.calculate_bounding_box_areas(results)
      
      return number_of_damaged, res_proportion, output_path

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
               elif are <= 120000:
                  proportion = 80
               else:
                  proportion = 100
               areas.append(proportion)
      res_proportion = sum(areas)/len(areas)
      if res_proportion >= 100:
         res_proportion = 100
      return res_proportion