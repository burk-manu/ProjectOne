import math
import sympy as sp
import os

import manager
import log

def basic_operations_module(user_input): # Funktion die für das Ausrechnen der Grundoperationen zuständig ist; Abkürzung bom
    try:
        solution = user_input
        solution = solution.replace("^","**")
        solution = sp.sympify(solution).evalf()
        if str(solution) == "zoo":
            return log.error("Division by Zero is not defined!", "Basic Operations Module", "201")
        else:
            try:
                if solution - int(solution) == 0:
                    solution = int(solution)
            except Exception:
                pass
                
        return solution
    except ZeroDivisionError:
        return log.error("Division by Zero is not defined!", "Basic Operations Module", "201")
    except OverflowError:
        return log.error("Overflow: The result is too big!", "Basic Operations Module", "203")
    except ValueError:
        return log.error("Invalid input: The operation could not be executed", "Basic Operations Module", "202") # Gibt einen Error zürück, falls der Input nicht der erwarteten Struktur entspricht