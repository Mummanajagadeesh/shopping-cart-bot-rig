import requests
import json
import re  # For searching the list format

# Step 1: Read text from ocr-detected-text.txt
with open('ocr-detected-text.txt', 'r') as ocr_file:
    ocr_text = ocr_file.read().strip()

# API details
url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'
api_key = 'AIzaSyDvDe7DO01mfWrUrcWFqLdZLKKPGC2X5uU'

headers = {
    'Content-Type': 'application/json'
}

# Step 2: Use the OCR-detected text in the prompt
prompt_text = f"""
The following text was detected from a scanned label: 
{ocr_text}

Now, check for barcode considering expected text size and spaces. 
Repair the detected text, it may have some errors.

**Important:**
I need the final output as a Python list named 'product_info' with **explicit values**, without using variables to store any intermediate information (like `name`, `type_category`, etc.).

The output should look like this:
```python
product_info = ["IPad retina Display", "Tablet", "0012458695691", 1, None, 0]

For example:
product_info = ["Apple", "Food", "123456789", 4, 50, 15]

Use the barcode information for accuracy improvement, and feel free to search for details online if needed.

"""

# Step 3: Prepare the payload for the API request
data = {
    "contents": [
        {
            "parts": [
                {"text": prompt_text}
            ]
        }
    ]
}

# Step 4: Make the POST request to the Gemini API
response = requests.post(f"{url}?key={api_key}", headers=headers, data=json.dumps(data))

if response.status_code == 200:
    # Step 5: Get the response JSON
    response_data = response.json()

    # Save the full response for reference in gemini-response.txt
    with open('gemini-response.txt', 'w') as f:
        json.dump(response_data, f, indent=4)

    # Step 6: Extract the exact answer (the "text" field)
    answer_text = response_data["candidates"][0]["content"]["parts"][0]["text"]

    # Save the filtered answer to gemini-response-filtered.txt
    with open('gemini-response-filtered.txt', 'w') as f:
        f.write(answer_text.strip())

    # Step 7: Use a regular expression to find the product_info list
    match = re.search(r'product_info\s*=\s*(\[[^\]]*\])', answer_text)

    if match:
        # Extract the list from the match group
        product_list = match.group(1)

        # Step 8: Write the extracted list to gemini-response-list.txt
        with open('gemini-response-list.txt', 'w') as f:
            f.write(product_list)

        print("All outputs saved: gemini-response.txt, gemini-response-filtered.txt, and gemini-response-list.txt")
    else:
        print("No product_info list found in the response.")

else:
    print("Failed:", response.status_code, response.text)
