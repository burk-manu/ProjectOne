import math
import sympy as sp

import log

logger = log.setup_logger(name=f"host.{__name__}")

def basic_operations_module(user_input): # function to calculate basic operations / terms
    try:
        solution = user_input.replace("^","**") # changes input into python language / syntax
        solution = sp.sympify(solution).evalf() # transforms solution into an numeric solutions
        if str(solution) == "zoo": # if answer is equal to 'zoo' which stands for complex infinity it returns an error
            logger.info("Division by Zero is not defined!") # error
        else: # if not it trys if the answer is an integer
            try:
                solution = float(solution) # converts solution to an integer
            except Exception:
                pass
        return solution
    except ZeroDivisionError:
        logger.info("Division by Zero is not defined!") # returns an division by zero error
    except OverflowError:
        logger.info("Overflow: The result is too big!") # returned an Overflow error
    except ValueError:
        logger.info("Invalid input: The operation could not be executed") # returns an unexpected error