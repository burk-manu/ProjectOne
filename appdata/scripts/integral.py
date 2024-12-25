import sympy as sp
import re

import manager
import log

logger = log.setup_logger(name=f"host.{__name__}") # setup logger

def integral_calculating_module(user_input):
    logger.debug("Integral calculation module started")
    try:
        if re.match(r"int\(\d+,\d+,[\w\+\-\*\/\^ ]+,\w\)", user_input): # pattern for integral regex
            integral = user_input[4:-1]
            begin_value, end_value, function, solve_for = integral.split(",")
            begin_value, end_value = float(begin_value), float(end_value)
            solve_for = sp.symbols(solve_for)
            function = function.replace("^", "**") # makes sure that python understands the input structure
            function = str(function) # converts into string
            function = re.sub(rf"(\d){solve_for}", rf"\1*{solve_for}", function) # adds missing multiplications signs
            function = sp.sympify(function) # converts into 'sympy language'
            integral = sp.integrate(function, (solve_for, begin_value, end_value)) # calculates integral
            return integral
        else:
            logger.info("Invalid Input")
    except ValueError:
        logger.info("Invalid Input")