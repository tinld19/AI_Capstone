from .inference.predict import DamageDetector
import numpy as np

class VisionServices:
   def detection_damage(self, file, image_paths):
      damageDetector = DamageDetector()
      number_of_damaged, res_proportion, output_path, img = damageDetector.predict(file, image_paths)
      return number_of_damaged, res_proportion, output_path, img