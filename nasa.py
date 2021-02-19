import nasapy
import os
from datetime import datetime
import urllib.request
import pandas as pd
import requests

nasa_api_key = 't6RqfybQcEKgLeB8QjAOGgSnhdT3hbcpTxPdfu5r'
nasa = nasapy.Nasa(key = nasa_api_key)

def picture_of_the_day():
    # Picture of the day
    d = datetime.now()
    #print(d)

    #Get the image data:
    apod = nasa.picture_of_the_day(date=d, hd=True) 
    return apod