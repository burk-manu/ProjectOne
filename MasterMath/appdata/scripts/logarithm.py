import math
import sympy as sp
import os

import manager
import log

def logarithm_calculation_module(user_input):
    if user_input.startswith("log10(") and user_input.endswith(")"):
        number = sp.sympify(user_input[6:-1])  # Extrahiere die Zahl aus der Eingabe
        logarithm = sp.log(number, 10)  # Berechne den Logarithmus zur Basis 10
        if str(logarithm.evalf()) == "zoo":
            return log.error("Invalid input: Logarithm can not be calculated ","Logarith Calculating Module","602")
        else:
            return logarithm.evalf()
    
    elif user_input.startswith("ln(") and user_input.endswith(")"):
        number = sp.sympify(user_input[3:-1])  # Extrahiere die Zahl aus der Eingabe
        logarithm = sp.log(number)  # Berechne den natürlichen Logarithmus
        if str(logarithm.evalf()) == "zoo":
            return log.error("Invalid input: Logarithm can not be calculated ","Logarith Calculating Module","602")
        else:
            return logarithm.evalf()
    
    elif user_input.startswith("log(") and user_input.endswith(")"):
        try:
            number, base = user_input[4:-1].split(",")
            number = sp.sympify(number.strip())  # Entferne Leerzeichen und sympify die Zahl
            base = sp.sympify(base.strip())  # Entferne Leerzeichen und sympify die Basis
            logarithm = sp.log(number, base)  # Berechne den Logarithmus zur gegebenen Basis
            if str(logarithm.evalf()) == "zoo": # Gibt einen Fehler aus wenn der Wert unendlich wird
                return log.error("Invalid input: Logarithm can not be calculated ","Logarith Calculating Module","602")
            else:
                return logarithm.evalf()
        except ValueError:
            return log.error("Invalid input: Make sure to use the structure log(NUMBER, BASE); Use log10() for base 10 or ln() for base e ","Logarith Calculating Module","602")
    else:
        return log.error("Invalid input: Make sure to use the structure log(NUMBER, BASE), log10(NUMBER) or ln(NUMBER) ","Logarith Calculating Module","601")