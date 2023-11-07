from flask import Flask, render_template, request, redirect, url_for, session, flash
from config import app
export FLASK_APP=app.py

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/features')
def features():
    return render_template('features.html')

if __name__ == "__main__":
    app.run(debug=True)
