from flask import Flask, render_template, request
import requests
import json
import config
from requests.models import requote_uri

import os
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    if request.method =="POST":
        city=request.form['city']
        country=request.form['country']
        api_key=config.api_key

        weather_url = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city},{country}&units=imperial')

        weather_data=weather_url.json()

        temp = weather_data['main']['temp']
        temp=round((temp-32)* 5/9)
        humidity=weather_data['main']['humidity']
        feels_like=weather_data['main']['feels_like']
        feels_like=round((feels_like-32)* 5/9)
        return render_template("result.html", temp=temp, humidity=humidity,city=city.capitalize(),country=country,feels_like=feels_like)
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)