import math
import sympy as sp
import os

import manager
import log

def basic_operations_module(user_input): # function to calculate basic operations / terms
    try:
        solution = user_input.replace("^","**") # changes input into python language / syntax
        solution = sp.sympify(solution).evalf() # transforms solution into an numeric solutions
        if str(solution) == "zoo": # if answer is equal to 'zoo' which stands for complex infinety it returns an error
            return log.error("Division by Zero is not defined!", "Basic Operations Module", "201") # error
        else: # if not it trys if the answer is an integer
            try:
                solution = int(solution) # converts solution to an integer
            except Exception:
                pass
                
        return solution
    except ZeroDivisionError:
        return log.error("Division by Zero is not defined!", "Basic Operations Module", "201") # returns an division by zero error
    except OverflowError:
        return log.error("Overflow: The result is too big!", "Basic Operations Module", "203") # returnd an Overflow error
    except ValueError:
        return log.error("Invalid input: The operation could not be executed", "Basic Operations Module", "202") # returns an unexcpected error