import cv2
import tkinter as tk
from tkinter import Button


def capture_photo():
    global cap
    ret, frame = cap.read()
    if ret:
        
        cv2.imwrite("captured_photo.jpg", frame)
        print("Photo captured and saved as 'captured_photo.jpg'")
        cv2.imshow("Captured Photo", frame)
    else:
        print("Failed to capture photo")


def close_app():
    global cap
    cap.release()
    cv2.destroyAllWindows()
    root.destroy()

ip_camera_url = 'http://172.16.36.160:8080/video'  
cap = cv2.VideoCapture(ip_camera_url)

if not cap.isOpened():
    print("Error: Could not access the IP camera")
    exit()


root = tk.Tk()
root.title("IP Camera Photo Capture")

capture_button = Button(root, text="Capture Photo", command=capture_photo)
capture_button.pack(pady=20)

exit_button = Button(root, text="Exit", command=close_app)
exit_button.pack(pady=20)


def update_frame():
    ret, frame = cap.read()
    if ret:
        cv2.imshow("IP Camera Stream", frame)
    
    root.after(10, update_frame)


update_frame()
root.mainloop()
