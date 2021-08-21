from flask import Flask, redirect, render_template
import flask

app = Flask(__name__)


@app.route('/home')
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/events')
def events():
    return render_template("events.html")


@app.route('/technical-trader')
def course1():
    return render_template("courses/course1.html")


@app.route('/option-trader')
def course2():
    return render_template("courses/course2.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/base')
def base():
    return render_template("base.html")


@app.route('/carousel')
def carousel():
    return render_template("carousel.html")


@app.route('/terms-and-conditions')
def terms():
    return render_template("terms-and-conditions.html")


if __name__ == '__main__':
    app.run(debug=True)
