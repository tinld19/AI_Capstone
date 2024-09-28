import os
from ultralytics import YOLO

DATA_YAML_PATH = '/root/AI_Capstone/src/vision/data/data.yaml'  
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
    patience=20,
    save_period=20,
    device=0            
)