# Import libraries
import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras.models import model_from_json
from flask import Flask, render_template, request, redirect
from keras.preprocessing import image
import uuid
import numpy as np
import re
import sys
import base64
import os

# Path to our saved model
sys.path.append(os.path.abspath("./model"))


# Initialize flask app
app = Flask(__name__)

# Model files
MODEL_ARCHITECTURE = './model/model.json'
MODEL_WEIGHTS = './model/model.h5'

# Load the model from external files
json_file = open(MODEL_ARCHITECTURE)
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

# Get weights into the model
model.load_weights(MODEL_WEIGHTS)


def convertImage(imgData1,filename):
    filepath='./images/'+filename+'.png';
    # create 'images' folder if it doesn't already exist
    dirname = os.path.dirname(filepath)
    if not os.path.exists(dirname):
        os.makedirs(dirname)

    imgstr = re.search(r'base64,(.*)', str(imgData1)).group(1)
    with open(filepath, 'wb') as output:
        output.write(base64.b64decode(imgstr))

@app.route('/')
def index():
    return render_template("index.html")

# clear images files on image folder
@app.route('/clearimages/')
def makeempty():
    mypath = "images"
    for root, dirs, files in os.walk(mypath):
        for file in files:
            os.remove(os.path.join(root, file))
    return redirect('/')

# create prediction
@app.route('/predict/', methods=['GET', 'POST'])
def predict():
    filename = str(uuid.uuid4()) #random name

    # Predict method
    imgData = request.get_data()
    convertImage(imgData,filename)

    #read image
    img = image.load_img('images/'+filename+'.png', target_size=(64, 64))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    out = model.predict(x)
    response = np.argmax(out, axis=1)
    pos=response[0]
    prediction="not found"
    if (pos == 0) :
        prediction="ba"
    elif (pos == 1) :
        prediction='ca'
    elif (pos == 2) :
        prediction='da'
    elif (pos == 3) :
        prediction='dha'
    elif (pos == 4) :
        prediction='ga'
    elif (pos == 5) :
        prediction='ha'
    elif (pos == 6) :
        prediction='ja'
    elif (pos == 7) :
        prediction='ka'
    elif (pos == 8) :
        prediction='la'
    elif (pos == 9) :
        prediction='ma'
    elif (pos == 10) :
        prediction='na'
    elif (pos == 11) :
        prediction='nga'
    elif (pos == 12) :
        prediction='nya'
    elif (pos == 13) :
        prediction='pa'
    elif (pos == 14) :
        prediction='ra'
    elif (pos == 15) :
        prediction='sa'
    elif (pos == 16) :
        prediction='ta'
    elif (pos == 17) :
        prediction='tha'
    elif (pos == 18) :
        prediction='wa'
    elif (pos == 19) :
        prediction='ya'

    return str(prediction)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
