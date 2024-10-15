import os
import sys

# Add the path to the YOLOv5 directory
sys.path.append('/home/jagadeesh97/Documents/RIG/cv/yolov5/')

# Set the correct path to your data.yaml file
DATA_PATH = '/home/jagadeesh97/Documents/RIG/cv/yolov5/Groceries.v7-2022-12-14-5-07pm.yolov5pytorch/data.yaml'

# Define command to run YOLOv5 training with python3
command = f"python3 train.py --img 640 --batch 16 --epochs 50 --data {DATA_PATH} --weights yolov5s.pt --project Grocery_Train --name exp --exist-ok"

# Run the training command
if __name__ == '__main__':
    os.system(command)
