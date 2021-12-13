""" Class for division"""
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """Division calculation object"""

    def get_result(self):
        """Performing division function for the values inheriting from the parent class"""
        result = self.values[0]
        for value in self.values[1:]:
            result = result / value
        return result