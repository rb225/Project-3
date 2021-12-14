"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET'])
def index_get():
    return IndexController.get()

@app.route("/basicform", methods=['GET'])
def calculator_get():
    return CalculatorController.get()

@app.route("/basicform", methods=['POST'])
def calculator_post():
    return CalculatorController.post()