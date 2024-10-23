import sys
import time
from PyQt5 import QtWidgets, QtCore, QtGui
import cv2
import threading
import subprocess

class LabelScannerApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Main window settings
        self.setWindowTitle("Label Scanner & Payment System")
        self.setGeometry(100, 100, 800, 600)

        # Timer for auto calibration (10 seconds)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.capture_image)

        # Scan label button
        self.scan_button = QtWidgets.QPushButton("Scan Label", self)
        self.scan_button.setGeometry(50, 50, 200, 50)
        self.scan_button.clicked.connect(self.start_scanning)

        # Detect text button
        self.ocr_button = QtWidgets.QPushButton("Detect Text (OCR)", self)
        self.ocr_button.setGeometry(50, 120, 200, 50)
        self.ocr_button.clicked.connect(self.detect_text)

        # Correct text button
        self.gemini_button = QtWidgets.QPushButton("Correct Text (Gemini API)", self)
        self.gemini_button.setGeometry(50, 190, 200, 50)
        self.gemini_button.clicked.connect(self.correct_text)

        # Generate QR code button
        self.qr_button = QtWidgets.QPushButton("Generate QR Code", self)
        self.qr_button.setGeometry(50, 260, 200, 50)
        self.qr_button.clicked.connect(self.generate_qr_code)

        # Output text area for OCR results
        self.ocr_output = QtWidgets.QTextEdit(self)
        self.ocr_output.setGeometry(300, 50, 400, 100)
        self.ocr_output.setReadOnly(True)

        # Output area for product information and QR code
        self.product_info = QtWidgets.QTextEdit(self)
        self.product_info.setGeometry(300, 180, 400, 150)
        self.product_info.setReadOnly(True)

        # Placeholder for the scanned image
        self.image_label = QtWidgets.QLabel(self)
        self.image_label.setGeometry(300, 350, 400, 200)
        self.image_label.setStyleSheet("border: 1px solid black")

    def start_scanning(self):
        self.timer.start(10000)  # Start a 10-second timer for scanning calibration
        self.ocr_output.setText("Scanning in progress...")

    def capture_image(self):
        self.timer.stop()  # Stop the timer after 10 seconds

        # Call your scanner.py code here to capture image and save as scanned_label.jpg
        subprocess.call(['python3', 'scanned_new.py'])

        # Display the scanned image
        pixmap = QtGui.QPixmap("scanned_label.jpg")
        self.image_label.setPixmap(pixmap.scaled(400, 200, QtCore.Qt.KeepAspectRatio))
        self.ocr_output.setText("Label scanned. Ready for OCR.")

    def detect_text(self):
        # Call your OCR detection code here
        subprocess.call(['python3', 'ocr_detect.py'])

        # Load the detected text and display
        with open("ocr-detected-text.txt", "r") as file:
            ocr_data = file.read()
        self.ocr_output.setText(ocr_data)

    def correct_text(self):
        # Call your Gemini API correction script
        subprocess.call(['python3', 'gemini-api.py'])

        # Load the corrected text and display
        with open("gemini-response-list.txt", "r") as file:
            corrected_data = file.read()
        self.product_info.setText(corrected_data)

    def generate_qr_code(self):
        # Call the QR code generation script
        subprocess.call(['python3', 'qr_code_updated.py'])

        # Load and display the generated QR code
        pixmap = QtGui.QPixmap("generated_qr_code.png")
        self.image_label.setPixmap(pixmap.scaled(400, 200, QtCore.Qt.KeepAspectRatio))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LabelScannerApp()
    window.show()
    sys.exit(app.exec_())
