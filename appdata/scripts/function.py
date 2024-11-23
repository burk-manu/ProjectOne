import sympy as sp
import re


import log

logger = log.setup_logger(name=f"host.{__name__}") # setup logger

def function_calculating_module(user_input): # calculates Zeros of a function, derivatives and antiderivatives
    if re.match(r"^f\(\w\)=[\w\+\-\*\/\^]+$",user_input):
        solve_for = sp.symbols(str(user_input[2]))
        cut = user_input.index("=")+1
        function = user_input[cut:] # extracting part after the 'f(x) = '
        function = function.replace("^", "**")
        function = str(function) # converts function into a string
        function = re.sub(rf"(\d){solve_for}", rf"\1*{solve_for}", function) # adds missing multiplication signs
        logger.debug(f"function was converted to the Python language")
        logger.debug(f"calculating zeros of the function")
        try:
            function = sp.sympify(function)  # converts string into a SymPy expression
            solutions = sp.solve(function, solve_for) # calculates zeros of the function
            integral = sp.integrate(function, solve_for)
            derivation1 = sp.diff(function, solve_for)
            derivation2 = sp.diff(derivation1, solve_for)
            derivation3 =sp.diff(derivation2, solve_for)
            numeric_solutions = [sol.evalf() for sol in solutions]  # changes zeros of the function into numeric values
            return f"""function f({solve_for}) = {function}
            Zeros of the function f(x):		{numeric_solutions}
            F({solve_for}) = 				{integral}
            f'({solve_for}) = 				{derivation1}
            f''({solve_for}) = 				{derivation2}
            f'''({solve_for}) = 				{derivation3}"""  # returnd the solution
        except sp.SympifyError:
            logger.info("Invalid input: The zeros of the function can not be calculated")
    else:
        logger.info("Invalid input: Make sure to use the structure 'f(x) = ' ")