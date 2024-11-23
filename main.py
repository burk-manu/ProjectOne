import os
import sys
import colorama

# Import necessary modules
path_scripts = os.path.join(os.getcwd(), r"appdata\scripts")
sys.path.insert(0, path_scripts)

import log
import manager
import console
import system
import acesscontrol
import wolframalpha_module

# Setup Logger
logger = log.setup_logger(name="host")

system.setup_keyboard()

def access_check(): # Checks system access control and handles errors.

    try:
        status = acesscontrol.accesscontrol()
        if status != "working":
            user_input = input("System errors detected. Start anyway? [YES / NO]: ").strip().lower()
            if user_input != "yes":
                exit()
        return status
    except Exception:
        logger.warning("Access control failed.")
        user_input = input("Start without guarantees? [YES / NO]: ").strip().lower()
        if user_input != "yes":
            exit()
        return "not working"

def main():
    
    try:
        
        logger.debug("Program started")

        # Check system status
        system_status = access_check()
        system.set_max_int_len(4300)

        # Write system status to a file
        system.document_writer("accesscontrol.config", "status", system_status)

        # Start the program
        manager.print_intro()
        logger.debug("Program initialized")

        previous_solution = None

        # default module is calculator
        module = "calculator"
        logger.debug("Default module set to calculator")

        while True:

            answer = None

            if module == "calculator":
                printable = colorama.Fore.WHITE + "▷ Enter a calculation: "
                logger.debug("Module set to calculator")
            elif module == "console":
                printable = colorama.Fore.LIGHTMAGENTA_EX + ">>> "
                logger.debug("Module set to console")
            elif module == "wolframalpha":
                printable = colorama.Fore.LIGHTCYAN_EX + "▷ Enter a calculation: "
                logger.debug("Module set to wolframalpha")
            else:
                module = "calculator"
                logger.debug("unknown module, defaulting to calculator")
                continue

            user_input = str(input(printable)).strip().replace(" ", "")

            if user_input == "calculator" or user_input == "console" or user_input == "wolframalpha":
                module = user_input
                logger.debug(f"Module changed to {module}")
                continue
            else:
                logger.debug("Received input from user")
            
            if module == "calculator":
                logger.debug("Calculator started")
                answer = manager.operation_assignment_module(user_input, previous_solution)
            elif module == "console":
                logger.debug("Console started")
                answer = console.console(user_input)
            elif module == "wolframalpha":
                logger.debug("WolframAlpha started")
                answer = wolframalpha_module.wolframalpha_query(user_input)
            else:
                logger.debug("Unknown module")
                module = "calculator"
                continue

            print(colorama.Fore.GREEN+ str(answer))

            if answer != None:
                previous_solution = answer

    except ZeroDivisionError as e:
        print(f"Unexpected error occurred: [{e}]")
        print("Contact: burk.manu.2022@ksz.edu-zg.ch for support.")


if __name__ == "__main__":
    main()