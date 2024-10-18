import torch

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Load an image to test the model (replace with any valid image file or use webcam frame)
img = 'https://c8.alamy.com/comp/2GTKFJ6/set-of-random-objects-2GTKFJ6.jpg'

# Run YOLOv5 inference on the image
results = model(img)

# Display results
results.show()
