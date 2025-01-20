# import required plug-ins
import re


# import required files
import log
import system
import prepare

import logarithm
import integral
import function
import squareroot
import basic_operations
import trigonometry

logger = log.setup_logger(name=f"host.{__name__}")


def print_intro(): # prints intro
    # defines colors
    reset = system.color_reset()
    orange = system.define_color(255, 165, 0)
    blue = system.define_color(0, 0, 255)
    white = system.define_color(255, 255, 255)

    texts = {
        ">>>  W E L C O M E    T O    P R O J E C T    O N E  <<<": orange,
        "including": white,
        "✦   M A S T E R   M ∀ T H   ✦": blue,
        "✦   W O L F R A M   A L P H A   ✦": blue,
        "✦   C O N S O L E   ✦": blue
    }

    system.clear_console()

    for text, color in texts.items():
        print(color + text.center(100, " ") + reset)
    
    logger.debug("Intro printed")

def programme_started():
    prepare.prepare()


def operation_assignment_module(user_input, ans): # Operation Assignment Module tries to figure out which kind of operation the input is
    logger.debug(f"manager received input from input loop | input: {user_input} ") # logs the input

    if re.search(r"(sin|cos|tan|cot|sec|csc)", user_input):
        user_input = trigonometry.calculate_trigonometric_functions(user_input) # replaces trigonometric functions with their values
        logger.debug(f"manager received input from trigonometry module | input: {user_input} ") # logs the input

    # The following RegEx patterns were created with help from AI
    operations = {
        r"^help$": lambda: system.open_document("userguide.txt"), # opens help document
        r"^sqrt\([+-]?\d+(\.\d+)?([Ee][+-]?\d+)?\)$": lambda: squareroot.square_root_calculating_module(user_input), # calculates square root
        r"^int\([+-]?\d+(\.\d+)?([Ee][+-]?\d+)?,[+-]?\d+(\.\d+)?([Ee][+-]?\d+)?,([+-]?\d+(\.\d+)?([Ee][+-]?\d+)?|[\w\+\-\*\/\%\^])+,\w\)$": lambda: integral.integral_calculating_module(user_input), # calculates an integral
        r"^f\(\w\)=[\w\+\-\*\/\^]+$": lambda: function.function_calculating_module(user_input), # calculates Zeros of functions
        r"^(log\([+-]?\d+(\.\d+)?([Ee][+-]?\d+)?,[+-]?\d+(\.\d+)?([Ee][+-]?\d+)?\)|ln\([+-]?\d+(\.\d+)?([Ee][+-]?\d+)?\)|log10\([+-]?\d+(\.\d+)?([Ee][+-]?\d+)?\))$": lambda: logarithm.logarithm_calculation_module(user_input), # calculates logarithms
        r"^([+-]?\d+(\.\d+)?([Ee][+-]?\d+)?|[\w\+\-\*\/\%\^\(\))])+$": lambda: basic_operations.basic_operations_module(user_input), # calculates basic operations
        }
    
    if "ans" in str(user_input):
        user_input = str(user_input).replace("ans", str(ans))

    for key, action in operations.items(): # iterates through the operations
        if re.match(key, user_input): # checks if the input follows the syntax of the operation

            solution = action()

            logger.debug(f"Operation Assignment Module received the solution: {solution}") # logs the solution
        
            return solution # returns the result of the operation
    
    logger.debug("Invalid input: The operation could not be executed") # logs an error
    return "Invalid input: The operation could not be executed" # returns an error if the input has an invalid syntax