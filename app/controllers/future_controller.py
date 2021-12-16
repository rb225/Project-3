from app.controllers.controller import ControllerBase
from flask import render_template

class FutureController(ControllerBase):
    @staticmethod
    def get():
        return render_template('future.html')