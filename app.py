from flask import Flask, request, render_template, redirect, url_for
import requests

with open(".env/api-key.pub", "r") as f:
    KEY = f.readline()

app = Flask(__file__)
title = "Weather app"

@app.route("/")
def dashboard():
    return render_template("index.html", title=title)


@app.route("/weather", methods=["POST"])
def weather():
    city = request.form.get("city")
    if city in [None,""]:
        return redirect("/")
    params = {"q": city, "appid": KEY, "units": "metric"}

    url = "https://api.openweathermap.org/data/2.5/weather"

    response = requests.get(url, params=params)
    data = response.json()
    response.close()

    return render_template("results.html", weather=data, title=f"Weather in {city}")
