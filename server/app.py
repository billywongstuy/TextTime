from flask import Flask, url_for, redirect, render_template, session, request

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def root():
    return "meow"

@app.route("/api/todo/confirm")
def todo_confirm():
    return render_template("todo_confirm.html")

@app.route("/api/ocr", methods=["GET"])
def ocr():
    return "quack"

app.debug = True;
app.run()
