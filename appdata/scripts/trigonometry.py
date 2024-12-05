import math
import re

import log

logger = log.setup_logger(name=f"host.{__name__}") # setup logger

def calculate_trigonometric_functions(user_input): # calculates trigonometric functions [sin, cos, tan, asin, acos, atan] [AI]
    logger.debug("Trigonometry calculation module started")
    # regular expressions for the trigonometric functions
    pattern = r"(sin|cos|tan|asin|acos|atan)\((-?\d+(\.\d+)?)\)"
    
    # function for every regex-match
    def replace_function(match):
        func = match.group(1)  # name of the function (sin, cos, ...)
        number = math.radians(float(match.group(2)))  # extract the number as a float
        # math function with dynamic getattr
        result = getattr(math, func)(number)
        logger.debug(f"replaced {func}({number}) with {result}")
        return str(result)  # replace match with calculated value
    
    # replace all trigonometric strings in the input
    while re.search(pattern, user_input):
        user_input = re.sub(pattern, replace_function, user_input)
    
    return user_input
