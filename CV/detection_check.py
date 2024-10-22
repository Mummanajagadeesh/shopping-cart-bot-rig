import cv2
import torch
import requests
import json

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Use 0 for the default camera or '/dev/video0'
ip_webcam_url = 0

cap = cv2.VideoCapture(ip_webcam_url)

if not cap.isOpened():
    print("Error: Unable to access the camera.")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Run YOLOv5 inference on the frame
    results = model(frame)
    detections = results.xyxy[0].cpu().numpy()
    
    for det in detections:
        xmin, ymin, xmax, ymax, conf, cls = det
        if int(cls) == 0:  # Assuming class 0 is 'person'
            center_x = (xmin + xmax) / 2
            center_y = (ymin + ymax) / 2

            if center_x < frame.shape[1] // 3:
                direction = 'left'
            elif center_x > 2 * frame.shape[1] // 3:
                direction = 'right'
            else:
                direction = 'forward'
            
            if center_y > frame.shape[0] * 0.8:
                direction = 'stop'
            
            print(f"Direction: {direction}")
            # Here you would call send_movement_command(direction)

    # Show the frame with detections
    cv2.imshow('Person Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
