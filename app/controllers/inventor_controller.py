from app.controllers.controller import ControllerBase
from flask import render_template

class InventorController(ControllerBase):
    @staticmethod
    def get():
        return render_template('inventor.html')