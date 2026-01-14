from flask import Flask, request, render_template
import requests
app=Flask(__name__)
@app.route("/")
def dashboard():
<<<<<<< HEAD
    return render_template("app.html")
@app.route("/weather",methods=["POST"])
=======
    # return "Welcome to our webpage"
    return render_template("app.html")
@app.route("/weather", methods=["GET"])
>>>>>>> fec0eb9930639f466ae0743be0dacf5acce6ec9b
def weather():
    city = request.form.get("city")
    api_key = "c1ee229ff0b96db89a52ea6fe44a2adb"
    url = "https://api.openweathermap.org/data/2.5/weather"

    if request.method.upper() == "GET":
        city = request.form.get("city")

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    
    return data
