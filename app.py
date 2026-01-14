from flask import Flask, request, render_template
import requests
app=Flask(__name__)
@app.route("/")
def dashboard():
    return "Welcome to our webpage"
@app.route("/weather")
def weather():
    #city = request.form.get("city")
    city="Nairobi"
    api_key = "c1ee229ff0b96db89a52ea6fe44a2adb"
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "city": city,
        "api_key": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    
    return data    
