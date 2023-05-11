from flask import *
import random
import os

app = Flask(__name__)
@app.route("/")
def home():
    lines = open('facts.txt').read().splitlines()
    randomLine =random.choice(lines)
    return render_template("home.html", fact=randomLine)

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
