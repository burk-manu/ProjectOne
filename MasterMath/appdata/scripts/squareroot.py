import math
import sympy as sp
import os

import manager
import log

def sqare_root_calculating_module(user_input): # sqaure root module berechnet die Quadratwurzel einer Zahl; Abkürzung sqrtcm
    if user_input.startswith("sqrt(") and user_input.endswith(")"): # überprüft ob die Eingabe dem format sqrt(INPUT) entspricht
        try: # überprüft ob es sich beim Input um eine Zahl handelt, die verarbeitet werden kann
            number = float(user_input[5:-1]) # extrahiert die Nummer aus dem Input
            return math.sqrt(number) # Rechnet die Wurzel aus und gibt diese zurück
        except ValueError: # Gibt einen Error zurück falls die Zahl nicht berechnet werden kann
            return log.error("Invalid number", "Square Root Calculating Module", "301")
    else:
        return log.error("Invalid input: The operation could not be executed", "Square Root Calculating Module", "302") # Gibt eine Fehler zurück wenn das Format nicht gleich sqrt(INPUT) ist