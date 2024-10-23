import requests
import cv2
import json

# Your OCR API key
api_key = 'K89371958988957'

# OCR API endpoint
url = 'https://api.ocr.space/parse/image'

# Path to the image
image_path = 'scanned_label.jpg'

# Open the image file
try:
    with open(image_path, 'rb') as f:
        # Send the POST request to OCR API
        response = requests.post(
            url,
            files={'filename': f},
            data={
                'apikey': api_key,
                'language': 'eng',  
            }
        )
except FileNotFoundError:
    print(f"Error: The file '{image_path}' was not found.")
    exit()

# Check for a successful request (status code 200)
if response.status_code == 200:
    try:
        # Parse the JSON response
        result = response.json()

        # Debug: print full response for troubleshooting
        print("Full API Response:", json.dumps(result, indent=4))

        # Check if 'ParsedResults' exists and has elements
        if 'ParsedResults' in result and len(result['ParsedResults']) > 0:
            # Extract parsed text
            parsed_text = result['ParsedResults'][0].get('ParsedText', '')

            # Check if OCR text is found
            if parsed_text:
                print("Detected Text:\n", parsed_text)

                # Save the detected text to a file
                with open('ocr-detected-text.txt', 'w') as text_file:
                    text_file.write(parsed_text)

                print("Detected text saved to ocr-detected-text.txt")
            else:
                print("No text was detected in the image.")
        else:
            print("Error: 'ParsedResults' not found or is empty in the API response.")

    except json.JSONDecodeError:
        print("Error: The response could not be parsed as JSON.")
else:
    # If the request failed, print the status code and error message
    print(f"Error: API request failed with status code {response.status_code}")
    print("Response content:", response.content)

# Display the image using OpenCV
img = cv2.imread(image_path)

if img is not None:
    cv2.imshow("Scanned Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Error: Could not read image from '{image_path}'")
