import math
import sympy as sp
import os
import re

import manager
import log

def function_calculating_module(user_input): # Das function calculating module berechnet die Nullstellen einer Funktion; Abkürzung fcm
    if re.match(r'^f\([a-z]\) = ',user_input[0:7]):
        solve_for = sp.symbols(str(user_input[2]))
        cut = user_input.index("=") + 1
        function = user_input[cut:] # Der Teil nach dem 'f(x) = ' wird extrahiert
        function = function.replace("^", "**") # Die Funktion wird angepasst so dass sie der 'Python-Sprache' entspricht
        function = str(function) # wandelt die Funtkion in einen String um
        function = re.sub(rf"(\d){solve_for}", rf"\1*{solve_for}", function) # Fügt die fehlenden Multiplikationszeichen ein
        log.log_entry(f"function was converted to the Python language; [function:{function}]", "Function Calculating Module")
        log.log_entry(f"calculating zeros of the function f({solve_for}): = {function}; solve for: {solve_for}", "Function Calculating Module")
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
            return log.error("Invalid input: The zeros of the function can not be calculated", "Function Calculating Module", "401")
    else:
        return log.error("Invalid input: Make sure to use the structure 'f(x) = ' ", "Function Calculating Module", "402")