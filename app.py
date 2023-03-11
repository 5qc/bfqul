from flask import Flask, render_template, redirect
import random

from getchannel import getchannels
from getvideo import getvideos
from searches import searches

app = Flask(__name__)

@app.route("/")
def home():
    print()
    return render_template("index.html", video=getvideos(getchannels(random.choice(searches))))

if __name__ == "__main__":
    app.run(debug=True, port=3000)