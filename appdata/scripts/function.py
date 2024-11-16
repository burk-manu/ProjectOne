import math
import sympy as sp
import os
import re

import manager
import log

logger = log.setup_logger(name=f"host.{__name__}")

def function_calculating_module(user_input): # Das function calculating module berechnet die Nullstellen einer Funktion; Abkürzung fcm
    if re.match(r"^f\(\w\) = [\w\+\-\*\/\^ ]+$",user_input):
        solve_for = sp.symbols(str(user_input[2]))
        cut = user_input.index("=") + 1
        function = user_input[cut:] # Der Teil nach dem 'f(x) = ' wird extrahiert
        function = function.replace("^", "**") # Die Funktion wird angepasst so dass sie der 'Python-Sprache' entspricht
        function = str(function) # wandelt die Funtkion in einen String um
        function = re.sub(rf"(\d){solve_for}", rf"\1*{solve_for}", function) # Fügt die fehlenden Multiplikationszeichen ein
        logger.debug(f"function was converted to the Python language")
        logger.debug(f"calculating zeros of the function")
        try:
            function = sp.sympify(function)  # String in SymPy-Ausdruck umwandeln [KI]
            solutions = sp.solve(function, solve_for) # Berechnet die Nullstellen der Funktion
            integral = sp.integrate(function, solve_for)
            derivation1 = sp.diff(function, solve_for)
            derivation2 = sp.diff(derivation1, solve_for)
            derivation3 =sp.diff(derivation2, solve_for)
            numeric_solutions = [sol.evalf() for sol in solutions]  # Wandelt die Nulletsllen in numerische Werte um [KI]
            return f"""function f({solve_for}) = {function}
            Zeros of the function f(x):		{numeric_solutions}
            F({solve_for}) = 				{integral}
            f'({solve_for}) = 				{derivation1}
            f''({solve_for}) = 				{derivation2}
            f'''({solve_for}) = 				{derivation3}"""  # sendet die Lösungen zurück an das oam
        except sp.SympifyError:
            return logger.info("Invalid input: The zeros of the function can not be calculated")
    else:
        return logger.info("Invalid input: Make sure to use the structure 'f(x) = ' ")