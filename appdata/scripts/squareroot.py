import math
import sympy as sp
import os
import re

import manager
import log

def sqare_root_calculating_module(user_input): # sqaure root module calculates the squareroot of a number
    if re.match(r"sqrt\(\d+\)", user_input): # checks if structure of input is 'sqrt(NUMBER)'
        try:
            number = float(user_input[5:-1]) # eextracts number from the input
            return math.sqrt(number) # returns the calculated solution of the sqare root
        except ModuleNotFoundError: # retruns an error if the number is invalid
            return log.error("Invalid number", "Square Root Calculating Module", "301") # returns an error
    else:
        return log.error("Invalid input: The operation could not be executed", "Square Root Calculating Module", "302") # returns an error if input doesn't follow the syntax