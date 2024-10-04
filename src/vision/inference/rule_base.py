import torch

def convert_model(): 
   weight_path = "/Users/mac/Documents/AI_Capstone/AI_Capstone/src/vision/weights/container_detection_ver1_1.pt"
   model = torch.load(weight_path)
   torch.save({"ema": model["ema"]}, "/Users/mac/Documents/AI_Capstone/AI_Capstone/src/vision/weights/container_detection_ver1_2.pt")
   print("Success")