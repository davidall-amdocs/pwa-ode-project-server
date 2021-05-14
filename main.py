# import os, io
# import pandas as pd
# import base64

# from flask import Flask, jsonify, request
# from google.cloud import vision

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceAccount.json'
# client = vision.ImageAnnotatorClient()

# app = Flask(__name__);
# @app.route("/", methods=["POST"])
# def testImage():
#     print("Image recived")
#     jsonInput = request.get_json()
#     if (jsonInput == None) :
#         return jsonify({ "status": "error on json" })
    
#     inputString = jsonInput["image"]
#     if (inputString == None) :
#         return jsonify({ "status": "error on string" })

#     img = base64.decodestring(inputString)
#     return jsonify({ "status": "ok", "image": img })

# def detectText(img):
#     with io.open(img, 'rb') as image_file:
#         content = image_file.read()

#     image = vision.Image(content = content)
#     response = client.document_text_detection(image = image)
#     return response.full_text_annotation.text

# if __name__ == "__main__":
#     app.run(debug = True, port = 4001)

# FILE_NAME = 'image10.png'
# FOLDER_PATH = r'C:\project\api\test\images\handwritten'
# text = detectText(os.path.join(FOLDER_PATH, FILE_NAME))
# print(text)

