import math
import sympy as sp
import os
import re

import manager
import log

logger = log.setup_logger(name=f"host.{__name__}")

def sqare_root_calculating_module(user_input): # sqaure root module calculates the squareroot of a number
    if re.match(r"^sqrt\(\d+(\.\d+)?\)$", user_input): # checks if structure of input is 'sqrt(NUMBER)'
        try:
            number = float(user_input[5:-1]) # eextracts number from the input
            return math.sqrt(number) # returns the calculated solution of the sqare root
        except ValueError: # retruns an error if the number is invalid
            return logger.info("Invalid number") # returns an error
    else:
        return logger.info("Invalid input: The operation could not be executed") # returns an error if input doesn't follow the syntax