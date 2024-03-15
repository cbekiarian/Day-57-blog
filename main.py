from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/05d737b1b139b2fdce11")
response.raise_for_status()
all_posts = response.json()

@app.route('/')
def home():


    return render_template("index.html",all_posts =all_posts )

@app.route("/post/<id>")
def posts(id):
    return render_template("post.html", post =all_posts[int(id)-1] )


if __name__ == "__main__":
    app.run(debug=True)
