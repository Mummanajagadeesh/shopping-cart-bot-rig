import cv2
import torch

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Use 0 for the first camera or /dev/video0
cap = cv2.VideoCapture(0)  # Change to "/dev/video0" if needed
if not cap.isOpened():
    print("Error: Unable to access the camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Run YOLOv5 inference on the captured frame
    results = model(frame)

    # Display the results
    results.show()

    # Exit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
