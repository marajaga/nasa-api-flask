from flask import (
    Flask,
    render_template, 
    redirect, 
    url_for, 
)
import nasapy
import os
from datetime import datetime
import requests
import nasa

from dotenv import load_dotenv
load_dotenv()

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
    app.run(threaded=True, debug=False, port=5000)


