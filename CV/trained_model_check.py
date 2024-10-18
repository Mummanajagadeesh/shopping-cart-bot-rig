from roboflow import Roboflow
import supervision as sv
import cv2

rf = Roboflow(api_key="") #W7Zp10EM8b5983DIhfmz
project = rf.workspace().project("groceries-6pfog")
model = project.version(6).model

result = model.predict("", confidence=40, overlap=30).json()

labels = [item["class"] for item in result["predictions"]]

detections = sv.Detections.from_roboflow(result)

label_annotator = sv.LabelAnnotator()
bounding_box_annotator = sv.BoxAnnotator()

image = cv2.imread("cd00481a3e82cb99590517fe7ab2c87f.jpeg")

annotated_image = bounding_box_annotator.annotate(
    scene=image, detections=detections)
annotated_image = label_annotator.annotate(
    scene=annotated_image, detections=detections, labels=labels)

sv.plot_image(image=annotated_image, size=(16, 16))
