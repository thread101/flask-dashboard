from flask import Flask, request, render_template
import requests
app=Flask(__name__)
@app.route("/")
def dashboard():
    # return "Welcome to our webpage"
    return render_template("app.html")
@app.route("/weather", methods=["GET"])
def weather():
    #city = request.form.get("city")
    city="Nairobi"
    api_key = "c1ee229ff0b96db89a52ea6fe44a2adb"
    url = "https://api.openweathermap.org/data/2.5/weather"

    if request.method.upper() == "GET":
        city = request.form.get("city")

    params = {
        "city": city,
        "api_key": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    
    return data
