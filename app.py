from flask import Flask, request, render_template, redirect, url_for
import requests

with open(".env/api-key.pub", "r") as f:
    KEY = f.readline()

app=Flask(__file__)

@app.route("/")
def dashboard():
    return render_template("index.html", title="Weather app")

@app.route("/weather", methods=["GET"])
def weather():
    city = request.args.get("city").capitalize()

    if city in [None, ""]:
        return redirect("/")

    params = {
        "q": city,
        "appid": KEY,
        "units": "metric"
    }

    url = "https://api.openweathermap.org/data/2.5/weather"

    try:
        response = requests.get(url, params=params)
        data = response.json()
        response.close()

    except Exception:
        data = {
            "Error" : "There was an issue processing your request"
        }
    
    return render_template("index.html", title=f"Results ({city})", data=data)
