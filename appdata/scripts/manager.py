# import required plug-ins
import math
import sympy as sp
import os
import colorama
import re
import time
import webbrowser
import datetime

# import required files
import log
import console
import prepare
import system

import logarithm
import integral
import function
import squareroot
import basic_operations


# dfinign space of variables and lists
operators = ["sqrt", "int","f", "log", "ln", "+", "-", "*", "/", "^", "%", "sin", "cos", "tan", "cot"] # Liste der verfügberen Operatoren

def programm_started(): # run when the programme starts
    prepare.prepare() # preparing and running background activities
    system.get_system_information()


# general functions [intro, open URLs]
def print_intro(): # prints intro
    print(colorama.Fore.BLUE + " ✦ M A S T E R   M ∀ T H ✦ ")
    print("")
    
def open_link_in_browser(url): # opens a specific URL in the browser
    webbrowser.open(url)
    log.log_entry(f"opening website with url: {url}", "Operation Assignment Module")
    return "opening website"


# Operatiosn Assignment Module: checks the input and forwards it to the relevant calculation module
def operation_assignment_module(user_input, ans):
    if "help" in user_input: # opens document with input structure, error-code meanings and other important informations
        open_link_in_browser("https://eduzg-my.sharepoint.com/:f:/g/personal/burk_manu_2022_ksz_edu-zg_ch/EviqcQd93dJOv9hP0eUGdMkBBppDHHHLWhCKwl_MPkYbLg?e=vY0rQG")
        return "opening documents"
    elif "ans" in user_input:
        user_input = user_input.replace("ans",str(ans))
    log.log_entry(f"Operation Assignment Module started [Input: {user_input}]", "Operation Assignment Module")
    for operator in operators: # the loop checks each element in the list 'operators'
        if operator in user_input: # checks if the operator is in the input
            log.log_entry(f"[User Input: '{user_input}' includes Operator: '{operator}']","Operation Assignment Module")
            try:
                if operator in ["sqrt"]:
                    log.log_entry("Square Root Calculating Module started", "Operation Assignment Module") # Logfile entry
                    solution = squareroot.sqare_root_calculating_module(user_input)
                    log.log_entry(f"received response from Square Root Calculating Module [response: {solution}]", "Operation Assignment Module") # Log eintrag
                    return solution
                elif operator in ["int"]:
                    log.log_entry("Integral Calculating Module started", "Operation Assignment Module") # Logfile entry
                    solution = integral.integral_calculating_module(user_input)
                    log.log_entry(f"received response from Integral Calculating Module [response: {solution}]", "Operation Assignment Module") # Logfile entry
                    return solution
                elif operator in ["f"]: # checks if input is a function
                    log.log_entry("Function Calculating Module started", "Operation Assignment Module") # Logfile entry
                    solution = function.function_calculating_module(user_input)
                    log.log_entry(f"received response from Function Calculating Module [response: {solution}]", "Operation Assignment Module") # Logfile entry
                    return solution
                elif operator in ["log", "ln"]: # checks if input is a logarithm
                    log.log_entry("Logarithm Calculating Module started", "Operation Assignment Module") # Logfile entry
                    solution = logarithm.logarithm_calculation_module(user_input)
                    log.log_entry(f"received response from Logarithm Calculating Module [response: {solution}]", "Operation Assignment Module") # Logfile entry
                    return solution
                elif operator in ["+", "-", "*", "/", "^", "%"]:
                    log.log_entry("Basic Operations Module started", "Operation Assignment Module") # Logfile entry
                    solution = basic_operations.basic_operations_module(user_input)
                    log.log_entry(f"received response from Basic Operations Module [response: {solution}]", "Operation Assignment Module") # Logfile entry
                    return solution
            except ValueError:
                return log.error("Value Error, your input is may to big to be handeld ","Operation Assignment Module","102")
    return log.error("Invalid input: The operation could not be executed", "Operation Assignment Module", "101") # returns an error if the input has an invalid syntax
