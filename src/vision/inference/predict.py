import os
import uuid
from PIL import Image
import matplotlib.pyplot as plt
from ultralytics import YOLO

model_path = '/Users/mac/Documents/AI_Capstone/AI_Capstone/src/vision/weights/best.pt'

class DamageDetector:
   def __init__(self, save_dir='/src/vision/image'):

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
      
      return number_of_damaged
