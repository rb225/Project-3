from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request, flash, redirect, url_for


class CalculatorController(ControllerBase):
    @staticmethod
    def post():

        # get the values out of the form
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']

        if request.form['value1'] == '' and request.form['value2'] == '':
            flash('Please enter valid input in both the fields')
        elif request.form['value1'] == '':
            flash('Please enter valid input for Value 1 field')
        elif request.form['value2'] == '':
            flash('Please enter valid input for Value 2 field')
        else:
            flash('Calculation is done successfully !!!!')

            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result)
        return render_template('basicform.html')

    @staticmethod
    def get():
        return render_template('basicform.html')