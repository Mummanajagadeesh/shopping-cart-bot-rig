import requests
import cv2

# Your OCR API key
api_key = 'K89371958988957'

# OCR API endpoint
url = 'https://api.ocr.space/parse/image'


image_path = 'scanned_label.jpg'


with open(image_path, 'rb') as f:
  
    response = requests.post(
        url,
        files={'filename': f},
        data={
            'apikey': api_key,
            'language': 'eng',  
        }
    )


result = response.json()


parsed_text = result.get('ParsedResults', [{}])[0].get('ParsedText', '')


print("Detected Text:\n", parsed_text)


with open('ocr-detected-text.txt', 'w') as text_file:
    text_file.write(parsed_text)

print("Detected text saved to ocr-detected-text.txt")

cv2.imshow("result", cv2.imread(image_path))
cv2.waitKey(0) 
cv2.destroyAllWindows()