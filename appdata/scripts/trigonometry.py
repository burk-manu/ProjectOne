import math
import re

def calculate_trigonometric_functions(user_input):
    # Regex für trigonometrische Funktionen mit einer Zahl oder einem Ausdruck in Klammern
    pattern = r"(sin|cos|tan|asin|acos|atan)\((-?\d+(\.\d+)?)\)"
    
    # Funktion, die für jedes Regex-Match die Berechnung durchführt
    def replace_function(match):
        func = match.group(1)  # Name der Funktion (sin, cos, ...)
        number = float(match.group(2))  # Extrahierte Zahl als Float
        # Verwende die math-Funktion dynamisch mit getattr
        result = getattr(math, func)(number)
        return str(result)  # Ersetze das Match durch den berechneten Wert
    
    # Ersetze alle trigonometrischen Funktionen im Eingabestring
    while re.search(pattern, user_input):
        user_input = re.sub(pattern, replace_function, user_input)
    
    return user_input

# Beispielaufruf
user_input = input("Enter a calculation with trigonometric functions: ")
result = calculate_trigonometric_functions(user_input)
print(result)
