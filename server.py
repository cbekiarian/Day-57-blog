from flask import Flask, render_template
import requests

import random
app =  Flask(__name__)
import datetime
@app.route("/")
def blog():
    return "hello world"

@app.route("/guess/<name_selected>")
def guesser(name_selected):
    response = requests.get(url= f"https://api.genderize.io?name={name_selected}")
    response.raise_for_status()
    gender =response.json()["gender"]
    response = requests.get(url=f"https://api.agify.io?name={name_selected}")
    response.raise_for_status()
    age = response.json()["age"]
    return render_template("index.html",name = name_selected,gender= gender,age= age )

@app.route("/blog")
def my_blog():
    my_url = "https://api.npoint.io/05d737b1b139b2fdce11"
    response = requests.get(url= my_url)
    response.raise_for_status()
    all_posts = response.json()
    print (all_posts)
    return render_template("blog.html", posts = all_posts)

if __name__ == "__main__":
    app.run(debug=True)