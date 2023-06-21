import cv2
import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import tempfile
import urllib.request
import requests
from dotenv import load_dotenv
load_dotenv()
import os
import warnings
warnings.filterwarnings("ignore")
import sys
sys.path.append('/home/ajay/Animations/AnimatedDrawings/')

cloudinary.config(
  cloud_name = "djvu7apub",
  api_key = os.getenv("API_KEY_CLOUD"),
  api_secret = os.getenv("API_SECRET"),
  secure = True
)

def main():
    url = 'http://0.0.0.0:7000/Animation'
    # print(url)
    # payload = {
    #     'motion': 'dab', 
    #     'image_url': ['https://res.cloudinary.com/djvu7apub/image/upload/v1685354924/rp7mmnyaoqlxcy3pej4c.jpg']
    #     }

    ans = cloudinary.uploader.upload('/home/ajay/Animations/AnimatedDrawings/examples/drawings/garlic.png', public_id = 'char3', overwrite = True)
    payload = {
        'motion': ['Motion'], 
        'image' : ans['secure_url'], 
        'image_url': [ans['secure_url']]
        }
    print('started')
    response = requests.post(url, json=payload)
    print(response.json())

if __name__ == '__main__':
    main()


