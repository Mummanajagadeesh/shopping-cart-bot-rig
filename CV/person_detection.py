import cv2
import torch
import requests

# Load YOLOv5 model
try:
    device = torch.device('cpu')  # Force CPU
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True, device=device)

except Exception as e:
    print(f"Error loading model: {e}")

# Set video source
cap = cv2.VideoCapture("/dev/video0")
if not cap.isOpened():
    print("Error opening video stream or file")
    exit()

def send_movement_command(direction):
    url = 'http://192.168.12.42/move'
    data = {'direction': direction}
    try:
        requests.post(url, json=data)
    except Exception as e:
        print(f"Error sending command: {e}")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    results = model(frame)

    detections = results.xyxy[0].cpu().numpy()
    for det in detections:
        xmin, ymin, xmax, ymax, conf, cls = det

        if int(cls) == 0:  # Assuming class '0' is the person class
            center_x = (xmin + xmax) / 2
            center_y = (ymin + ymax) / 2

            if center_x < frame.shape[1] // 3:
                send_movement_command('left')  
            elif center_x > 2 * frame.shape[1] // 3:
                send_movement_command('right') 
            else:
                send_movement_command('forward')  

            if center_y > frame.shape[0] * 0.8:
                send_movement_command('stop')  

    cv2.imshow('Person Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
