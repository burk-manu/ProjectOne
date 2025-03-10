import sympy as sp
import re

import log

logger = log.setup_logger(name=f"host.{__name__}")  # setup logger

def calculate_trigonometric_functions(user_input):  # calculates trigonometric functions [sin, cos, tan, asin, acos, atan] [AI]
    logger.debug("Trigonometry calculation module started")
    
    # Regular expressions for the trigonometric functions
    pattern = r"(sin|cos|tan|asin|acos|atan)\((-?\d+(\.\d+)?)\)"
    
    # Function for every regex match
    def replace_function(match):
        func = match.group(1)  # Name of the function (sin, cos, ...)
        number = sp.rad(float(match.group(2)))  # Convert the number to radians using sympy's rad function
        # sympy function with dynamic getattr
        result = getattr(sp, func)(number).evalf()  # Calculate result and evaluate it numerically
        logger.debug(f"replaced {func}({number}) with {result}")
        return str(result)  # Replace match with calculated value
    
    # Replace all trigonometric strings in the input
    while re.search(pattern, user_input):
        user_input = re.sub(pattern, replace_function, user_input)
    if "zoo" in user_input:
        return "diverges towards complex infinity"
    return user_input