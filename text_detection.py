import os, io
import pandas as pd
import base64

from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccount.json'
client = vision.ImageAnnotatorClient()

def detectText(img):
    image = vision.Image(content = img)

