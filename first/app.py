from flask import Flask, request
from flask_restful import Api, Resource
import keras
from PIL import Image
import numpy as np
from dotenv import load_dotenv
from pyngrok import ngrok
import os

load_dotenv()

model = keras.models.load_model(r"D:\VS projects\first\Model.h5")

# Class names
CLASS_NAMES = ['cardboard', 'glass', 'metal', 'paper', 'plastic', 'trash']

def preprocess_image(image, target_size):
    if image.mode != 'RGB':
        image = image.convert('RGB')
    # Resize the image
    image = image.resize(target_size)
    # Convert the image to a NumPy array
    image_array = np.array(image)
    # Add a batch dimension
    image_array = np.expand_dims(image_array, axis=0)
    # Normalize the image
    image_array = image_array / 255.0
    return image_array

def predict(img):
    # Preprocess the image
    img_array = preprocess_image(img, (224, 224))
    # Predict
    pred = model.predict(img_array, verbose=0)
    return CLASS_NAMES[np.argmax(pred)]

class Predict(Resource):
    def post(self):
        file = request.files['image']
        img = Image.open(file)
        return {"result": predict(img)}

app = Flask(__name__)
api = Api(app)

api.add_resource(Predict, "/classify")

NGROK_AUTH = os.getenv("NGROK_AUTH")
port = 5000
ngrok.set_auth_token(NGROK_AUTH)
tunnel = ngrok.connect(port, domain="miserably-current-lioness.ngrok-free.app")
print("Public URL :", tunnel.public_url)
app.run(host="0.0.0.0", port=5000)