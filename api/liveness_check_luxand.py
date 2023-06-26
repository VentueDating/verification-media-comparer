#!/usr/bin/env python3

import requests
import json

API_TOKEN = "f8771d1dc6184dd7bc2274074def937a"
def liveness_check_luxand(image_path):
    url = "https://api.luxand.cloud/photo/liveness"
    headers = {"token": API_TOKEN}

    if image_path.startswith("https://"):
        files = {"photo": image_path}
    else:
        files = {"photo": open(image_path, "rb")}

    response = requests.post(url, headers=headers, files=files)
    result = json.loads(response.text)

    if response.status_code == 200:
        return response.json()
    else:
        print("Can't recognize people:", response.text)
        return None


'''
Usage:
image_path = "../liveness_pics/fake1.JPG"
result = liveness(image_path)
print(result)
'''
