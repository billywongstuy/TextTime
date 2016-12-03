from flask import Flask, url_for, redirect, render_template, session, request, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route("/", methods=["POST","GET"])
def root():
    return "meow"

@app.route("/api/todo-confirm")
def todo_confirm():
    return render_template("todo_confirm.html")

@app.route("/api/ocr", methods=["GET"])
def ocr():
    return "quack"


@app.route("/me", methods=["POST","GET"])
def pock():
	with open("static/jquery-3.1.1.min.js","r") as myfile:
		data=myfile.read()
		print (data)
	return send_from_directory("static","jquery-3.1.1.min.js")


app.debug = True;
app.run()
