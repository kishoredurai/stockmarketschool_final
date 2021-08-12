
from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route('/home')
@app.route("/")
def home():
    # return "<p>Hello, World!</p>"
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/events')
def events():
    return render_template("live-webinar.html")


@app.route('/course1')
def course1():
    return render_template("courses/course1.html")


@app.route('/course2')
def course2():
    return render_template("courses/course2.html")
@app.route('/contact')
def contact():
   return render_template("contact.html")
@app.route('/base')
def base():
   return render_template("base.html")
if __name__ == '__main__':
    app.run(debug=True)
