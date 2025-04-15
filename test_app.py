import requests
import base64
import os
import json
import time
import sys

def test_api():
    # This is a simple test to verify the API endpoint
    # In a real scenario, you would need to send an actual image
    print("Testing API endpoint...")
    
    # Check if the server is running
    try:
        response = requests.get('http://localhost:5000/')
        print("Server is running!")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Make sure the Flask app is running.")
        print("Run 'python app.py' in a separate terminal window first.")
        sys.exit(1)
    
    # Create a simple test image (1x1 pixel)
    from PIL import Image
    import io
    
    img = Image.new('RGB', (1, 1), color='white')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='JPEG')
    img_byte_arr = img_byte_arr.getvalue()
    
    # Convert to base64
    img_base64 = base64.b64encode(img_byte_arr).decode('utf-8')
    
    # Send request to the API
    try:
        print("Sending test image to API...")
        response = requests.post(
            'http://localhost:5000/api/process_frame',
            json={'image': f'data:image/jpeg;base64,{img_base64}'}
        )
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api() 