import os
from ultralytics import YOLO

DATA_YAML_PATH = '/Users/mac/Documents/AI_Capstone/AI_Capstone/src/vision/data/data.yaml'  
MODEL_NAME = 'yolov8s.pt'     
EPOCHS = 100                  
BATCH_SIZE = 16               
IMG_SIZE = 640                
SAVE_PATH = './runs/train'    

assert os.path.exists(DATA_YAML_PATH), "File dữ liệu không tồn tại!"

model = YOLO(MODEL_NAME)

model.train(
    data=DATA_YAML_PATH,
    epochs=EPOCHS,  
    batch=BATCH_SIZE,   
    imgsz=IMG_SIZE,   
    project=SAVE_PATH,  
    name='yolov8s_custom',   
    cache=True,              
    verbose=True             
)