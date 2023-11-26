#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/Home")
def front_page():
    return render_template('home.html')

@app.route("/About")
def about_page():
    return render_template('about.html')

@app.route("/Services")
def our_service():
    return render_template('service.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
