import sympy as sp

import log

logger = log.setup_logger(name=f"host.{__name__}")

def basic_operations_module(user_input): # function to calculate basic operations / terms
    logger.debug("Basic Operations Module received input from Operation Assignment Module") # logs the input
    try:
        solution = user_input.replace("^","**") # changes input into python language / syntax
        solution = sp.sympify(solution).evalf() # transforms solution into an numeric solutions
        if str(solution) == "zoo": # zoo stands for complex infinity
            return "diverges towards complex infinity"
        else: # if the solution is a number
            try:
                solution = float(solution) # converts solution to a float
            except Exception:
                pass
        logger.debug(f"Basic Operations Module returned {solution}") # returns the solution
        return solution
    except ZeroDivisionError:
        logger.info("Division by Zero is not defined!") # returns an division by zero error
    except OverflowError:
        logger.info("Overflow: The result is too big!") # returns an Overflow error
    except ValueError:
        logger.info("Invalid input: The operation could not be executed") # returns an unexpected error