from flask import Flask, render_template
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
import base64
import io

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["CACHE_TYPE"] = "null"

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/getimage")
def get_img():
    latent_vec = np.random.randn(1,128)
    img = np.squeeze(generator(latent_vec))
    img = keras.preprocessing.image.array_to_img(img)
    img.save('static/out1.jpg')
    print('new image saved1')
    return ("nothing")

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    print('cache refreshed?')
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__':
    generator = load_model('generator_naruto3.h5')
    app.run()
    

