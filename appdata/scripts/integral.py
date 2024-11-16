import math
import sympy as sp
import os
import re

import manager
import log

logger = log.setup_logger(name=f"host.{__name__}")

def integral_calculating_module(user_input):
    try:
        if re.match(r"int\(\d+,\d+,[\w\+\-\*\/\^ ]+,\w\)", user_input):
            integral = user_input[4:-1]
            begin_value, end_value, function, solve_for = integral.split(",")
            begin_value, end_value = float(begin_value), float(end_value)
            solve_for = sp.symbols(solve_for)
            function = function.replace("^", "**") # makes sure that python understands the inputstructure
            function = str(function) # wandelt die Funtkion in einen String um
            function = re.sub(rf"(\d){solve_for}", rf"\1*{solve_for}", function) # adds missing multiplications signs
            function = sp.sympify(function) # converts into 'sympy language'
            integral = sp.integrate(function, (solve_for, begin_value, end_value)) # calculates intergral
            return integral
        else:
            logger.info("Invalid Input", "Integral Calculating Module", "501")
    except ValueError:
        logger.info("Invalid Input", "Integral Calculating Module", "502")