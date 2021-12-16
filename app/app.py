"""A simple flask web app"""
from flask import Flask
from app.controllers.index_controller import IndexController
from app.controllers.calculator_controller import CalculatorController
from app.controllers.article_controller import Article1Controller
from app.controllers.article2_controller import Article2Controller
from app.controllers.future_controller import FutureController
from app.controllers.inventor_controller import InventorController
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
@app.route("/article1", methods=['GET'])
def article1_get():
    return Article1Controller.get()

@app.route("/article2", methods=['GET'])
def article2_get():
    return Article2Controller.get()

@app.route("/future", methods=['GET'])
def future_get():
    return FutureController.get()

@app.route("/inventor", methods=['GET'])
def inventor_get():
    return InventorController.get()