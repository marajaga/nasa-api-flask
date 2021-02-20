import nasapy
import os
from datetime import datetime
import requests

nasa_api_key = os.getenv("NASA_API_KEY")
nasa = nasapy.Nasa(key = nasa_api_key)

def picture_of_the_day():
    # Picture of the day
    d = datetime.now()
    print(d)

    #Get the image data:
    #apod = nasa.picture_of_the_day(date=d, hd=True) 
    apod = nasa.picture_of_the_day(date=d, hd=True)     
    return apod
