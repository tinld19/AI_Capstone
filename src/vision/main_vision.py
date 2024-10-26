from .inference.predict import DamageDetector
import numpy as np

class VisionServices:
   def detection_damage(self, file, image_paths):
      damageDetector = DamageDetector()
      number_of_damaged, res_proportion, output_path, img = damageDetector.predict(file, image_paths)
      return number_of_damaged, res_proportion, output_path, img
   
# if __name__ == "__main__":
#    image_paths = "/Users/mac/Documents/AI_Capstone/AI_Capstone/src/vision/image/img20210724124936-jpg.jpg"
#    visionServices = VisionServices()
#    number_of_damaged, areas = visionServices.detection_damage(image_paths)
#    print(f"có {len(number_of_damaged)} lỗi")
#    print("tỉ lệ hư hỏng trung bình của container: {:.2f}%".format(areas))
   