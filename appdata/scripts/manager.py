# import required plug-ins
import sympy as sp
import colorama
import re


# import required files
import log
import system

import logarithm
import integral
import function
import squareroot
import basic_operations

logger = log.setup_logger(name=f"host.{__name__}")


def print_intro(): # prints intro
    print(colorama.Fore.BLUE + " ✦   M A S T E R   M ∀ T H   ✦ ")
    print("")




def operation_assignment_module(user_input, ans): # Operation Assignment Module tries to figure out which kind of operation the input is
    logger.debug("manager received input from input loop")
    operations = {
        r"^help$": lambda: system.open_link_in_browser("https://eduzg-my.sharepoint.com/:f:/g/personal/burk_manu_2022_ksz_edu-zg_ch/EviqcQd93dJOv9hP0eUGdMkBBppDHHHLWhCKwl_MPkYbLg?e=vY0rQG"), # opens help document
        r"^sqrt\(\d+(\.\d+)?\)$": lambda: squareroot.sqare_root_calculating_module(user_input), # calculates squareroot
        r"^int\(\d+,\d+,[\w\+\-\*\/\^]+,\w\)$": lambda: integral.integral_calculating_module(user_input), # calculates an integral
        r"^f\(\w\)=[\w\+\-\*\/\^]+$": lambda: function.function_calculating_module(user_input), # calculates Zeros of functions
        r"^(log\(\d+\, \d+\)|ln\(\d+\)|log10\(\d+\))$": lambda: logarithm.logarithm_calculation_module(user_input), # calculates logarithms
        r"^[\d\+\-\*\/\%\^]+$": lambda: basic_operations.basic_operations_module(user_input), # calculates basic operations
        }
    if "ans" in str(user_input):
        user_input = str(user_input).replace("ans", str(ans))

    for key, action in operations.items():
        if re.match(key, user_input):
            logger.debug("manager is sending back the result(s)")
            return action()
    
    logger.info("Invalid input: The operation could not be executed") # returns an error if the input has an invalid syntax
    return "Invalid input: The operation could not be executed"