from flask import Flask, render_template, request
from datetime import date
import time
import requests


app = Flask(__name__)


def weather_app(name):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={name}&appid=8d17a970989baecebfb248160af5c132"
    data = requests.get(url).json()
    return data


d = date.today()
@app.route('/')
def home():
    name = "Jalandhar"
    weather = weather_app(name)
    tm = int(weather['main']['temp']-273.15)
    v = weather['visibility']/1000
    icon = weather['weather'][0]['icon']
    ico = f"http://openweathermap.org/img/wn/{icon}@2x.png"
    return render_template('index.html', weather = weather, d = d, tm = tm, v=v, ico=ico)

@app.route('/new')
def search_name():
    
    if request.method == 'GET':
        name = request.args['name']
        weather = weather_app(name)
        if weather['cod'] == "404":
            name = "Jalandhar"
            weather = weather_app(name)
            tm = int(weather['main']['temp']-273.15)
            v = weather['visibility']/1000
            icon = weather['weather'][0]['icon']
            ico = f"http://openweathermap.org/img/wn/{icon}@2x.png"
            return render_template('index.html', weather = weather, d = d, tm = tm, v=v, ico=ico, message="Sorry! no city found")
        else:
            tm = int(weather['main']['temp']-273.15)
            v = weather['visibility']/1000
            icon = weather['weather'][0]['icon']
            ico = f"http://openweathermap.org/img/wn/{icon}@2x.png"
            return render_template('index.html', weather = weather, d = d, tm = tm, v=v, ico=ico)
        
    
if __name__ == "__main__":
    app.run(debug=True)