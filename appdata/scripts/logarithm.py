import math
import sympy as sp
import os

import manager
import log

logger = log.setup_logger(name=f"host.{__name__}") # setup logger

def logarithm_calculation_module(user_input):
    if user_input.startswith("log10(") and user_input.endswith(")"):
        number = sp.sympify(user_input[6:-1])  # extracts the number from the input
        logarithm = sp.log(number, 10)  # calculates the logarithm to base 10
        if str(logarithm.evalf()) == "zoo":
            logger.info("Invalid input: Logarithm can not be calculated")
        else:
            return logarithm.evalf()
    
    elif user_input.startswith("ln(") and user_input.endswith(")"):
        number = sp.sympify(user_input[3:-1])  # extracts the number from the input
        logarithm = sp.log(number)  # calculates the natural logarithm
        if str(logarithm.evalf()) == "zoo":
            logger.info("Invalid input: Logarithm can not be calculated")
        else:
            return logarithm.evalf()
    
    elif user_input.startswith("log(") and user_input.endswith(")"):
        try:
            number, base = user_input[4:-1].split(",")
            number = sp.sympify(number.strip())  # delete whitespaces and sympify the number
            base = sp.sympify(base.strip())  # delete whitespaces and sympify the base
            logarithm = sp.log(number, base)  # calculates the logarithm to the given base
            if str(logarithm.evalf()) == "zoo": # returns an error if the result is complex infinity
                logger.info("Invalid input: Logarithm can not be calculated")
            else:
                return logarithm.evalf()
        except ValueError:
            logger.info("Invalid input: Make sure to use the structure log(NUMBER, BASE); Use log10() for base 10 or ln() for base e")
    else:
        logger.info("Invalid input: Make sure to use the structure log(NUMBER, BASE), log10(NUMBER) or ln(NUMBER)")