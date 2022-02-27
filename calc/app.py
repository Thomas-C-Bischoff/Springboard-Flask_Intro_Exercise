# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request
app = Flask(__name__)

@app.route("/add")
def add_page():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a, b))

@app.route("/sub")
def sub_page():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a, b))

@app.route("/mult")
def mult_page():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a, b))

@app.route("/div")
def div_page():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a, b))

operators = {"add":add, "sub":sub, "mult":mult, "div":div}

@app.route("/math/<operator>")
def math_page(operator):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(operators[operator](a, b))