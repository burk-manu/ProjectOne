import math
import re

def calculate_trigonometric_functions(user_input):
    # reular expressions for the triconometric functions
    pattern = r"(sin|cos|tan|asin|acos|atan)\((-?\d+(\.\d+)?)\)"
    
    # function for every regex-match
    def replace_function(match):
        func = match.group(1)  # name of the function (sin, cos, ...)
        number = float(match.group(2))  # extract the number as a float
        # math function with dynamic getattr
        result = getattr(math, func)(number)
        return str(result)  # replace match with calculated vlaue
    
    # replace all triconometric strings in the input
    while re.search(pattern, user_input):
        user_input = re.sub(pattern, replace_function, user_input)
    
    return user_input
