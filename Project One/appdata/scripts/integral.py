import math
import sympy as sp
import os
import re

import manager
import log


def integral_calculating_module(user_input):
    try:
        if user_input.startswith("int(") and user_input.endswith(")"):
            integral = user_input[4:-1]
            begin_value, end_value, function, solve_for = integral.split(",")
            begin_value, end_value = float(begin_value), float(end_value)
            solve_for = sp.symbols(solve_for)
            function = function.replace("^", "**") # Die Funktion wird angepasst so dass sie der 'Python-Sprache' entspricht
            function = str(function) # wandelt die Funtkion in einen String um
            function = re.sub(rf"(\d){solve_for}", rf"\1*{solve_for}", function) # Fügt die fehlenden Multiplikationszeichen ein
            function = sp.sympify(function)
            integral = sp.integrate(function, (solve_for, begin_value, end_value))
            return integral
        else:
            return log.error("Invalid Input", "Integral Calculating Module", "501")
    except ValueError:
        return log.error("Invalid Input", "Integral Calculating Module", "502")