from flask import (
    Flask,
    render_template, 
    redirect, 
    url_for, 
)
import nasapy
import os
from datetime import datetime
from IPython.display import Image,display,Audio
from gtts import gTTS
from datetime import datetime
import urllib.request
import pandas as pd
import requests
import nasa

app = Flask(__name__)

@app.route('/', methods=["GET"])
def home():
    apod = nasa.picture_of_the_day()
    print(apod)
    return render_template('pages/home.html', url = apod['url'], apod = apod)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, port=3000)


