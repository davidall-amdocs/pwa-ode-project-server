import os, io
import pandas as pd
import base64

from google.cloud import vision

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccount.json'
client = vision.ImageAnnotatorClient()

def detectText(imgText):
    imgTextEnc = imgText.encode('utf-8')
    with open('decoded_image.png', 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(imgTextEnc)
        image = vision.Image(content = decoded_image_data)
        textDetected = client.document_text_detection(image = image)
        finalText = textDetected.full_text_annotation.text.replace("\n", "")
        finalText = finalText.replace(" ", "")
        return finalText



