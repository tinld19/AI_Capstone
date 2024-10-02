from inference.predict import DamageDetector

class VisionServices:
   def detection_damage(image_paths):
      damageDetector = DamageDetector()
      number_of_damaged = damageDetector.predict(image_paths)
      return number_of_damaged