import sys
import time
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QImage, QPixmap
from PyQt5.QtCore import QTimer
from scanner import Scanner
from scanned_new import scan_and_save_final_image
from ocr_detect import detect_text_in_image
from gemini_api import spell_correct_and_process
from qr_code_updated import generate_qr_code, products

class LabelScannerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.timer = QTimer()
        self.timer.setInterval(10000)  # 10 seconds for automatic calibration
        self.timer.timeout.connect(self.auto_finalize_scan)

        self.product_count = 0  # Track the number of products scanned

    def initUI(self):
        self.setWindowTitle('Product Label Scanner')
        self.setGeometry(100, 100, 800, 600)

        # Set up layout
        self.layout = QVBoxLayout()

        # Labels to show information
        self.scan_image_label = QLabel('Scanned Image will appear here', self)
        self.ocr_text_label = QLabel('OCR Text will appear here', self)
        self.product_info_label = QLabel('Product Info will appear here', self)
        self.qr_code_label = QLabel('QR Code will appear here', self)

        # Buttons
        self.scan_button = QPushButton('Scan Label', self)
        self.scan_button.clicked.connect(self.start_scan)

        self.ocr_button = QPushButton('OCR Detect Text', self)
        self.ocr_button.clicked.connect(self.detect_text)

        self.process_button = QPushButton('Process Product Info', self)
        self.process_button.clicked.connect(self.process_product)

        self.qr_button = QPushButton('Generate QR Code', self)
        self.qr_button.clicked.connect(self.generate_qr)

        # Adding widgets to layout
        self.layout.addWidget(self.scan_image_label)
        self.layout.addWidget(self.scan_button)
        self.layout.addWidget(self.ocr_text_label)
        self.layout.addWidget(self.ocr_button)
        self.layout.addWidget(self.product_info_label)
        self.layout.addWidget(self.process_button)
        self.layout.addWidget(self.qr_code_label)
        self.layout.addWidget(self.qr_button)

        # Set central widget and layout
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def start_scan(self):
        # Step 1: Scan the label
        self.timer.start()  # Start the 10-second timer for calibration
        self.scanner_thread = threading.Thread(target=self.calibrate_and_scan)
        self.scanner_thread.start()

    def calibrate_and_scan(self):
        scanner = Scanner()
        scanner.run()  # Assuming it opens trackbars and runs scanner.py logic

    def auto_finalize_scan(self):
        # Finalize after 10 seconds
        self.timer.stop()
        scan_and_save_final_image()  # Using scanned_new.py logic to save image
        self.display_image('scanned_label.jpg')

    def display_image(self, image_path):
        image = QImage(image_path)
        pixmap = QPixmap.fromImage(image)
        self.scan_image_label.setPixmap(pixmap)

    def detect_text(self):
        # Step 2: OCR detection
        detected_text = detect_text_in_image('scanned_label.jpg')
        self.ocr_text_label.setText(detected_text)

    def process_product(self):
        # Step 3: Process text with gemini API
        product_data = spell_correct_and_process('ocr-detected-text.txt')
        # Append product details to global dictionary
        self.product_count += 1
        products[self.product_count] = product_data
        self.product_info_label.setText(str(product_data))

    def generate_qr(self):
        # Step 4: Generate QR code
        generate_qr_code(products)
        self.qr_code_label.setText('QR Code generated for UPI payment!')

def main():
    app = QApplication(sys.argv)
    ex = LabelScannerApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
