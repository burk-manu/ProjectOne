import math
import re

import log

logger = log.setup_logger(name=f"host.{__name__}") # setup logger

def square_root_calculating_module(user_input): # square root module calculates the square root of a number
    logger.debug(f"Square Root Module received input from Operation Assignment Module | input: {user_input}") # logs the
    if re.match(r"^sqrt\([+-]?\d+(\.\d+)?([Ee][+-]?\d+)?\)$", user_input): # checks if structure of input is 'sqrt(NUMBER)'
        try:
            number = float(user_input[5:-1]) # extracts number from the input
            return math.sqrt(number) # returns the calculated solution of the square root
        except ValueError: # returns an error if the number is invalid
            logger.info("Invalid number") # returns an error
    else:
        logger.info("Invalid input: The operation could not be executed") # returns an error if input doesn't follow the syntax