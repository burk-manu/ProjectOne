import logging
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
        sys.set_int_max_str_digits(4300)

        # Write system status to a file
        system.document_writer("accesscontrol.config", "status", system_status)

        # Start the program
        manager.print_intro()
        logger.debug("Program initialized")

        previous_solution = None

        while True:
            user_input = input(colorama.Fore.WHITE + "▷ Enter a calculation: ").strip().replace(" ", "")
            if user_input == "console":
                logger.debug("Console started")
                while True:
                    console_output = console.console(input(colorama.Fore.LIGHTMAGENTA_EX + ">>> ").strip())
                    if console_output == "break":
                        logger.debug("Console stopped")
                        break
                    elif console_output:
                        print(colorama.Fore.LIGHTMAGENTA_EX + "▸", console_output)
            else:
                solution = manager.operation_assignment_module(user_input, previous_solution)
                logger.debug("Received response from Operation Assignment Module")
                print(colorama.Fore.GREEN + str(solution))
                if solution != None:
                    previous_solution = solution

    except ZeroDivisionError as e:
        print(f"Unexpected error occurred: [{e}]")
        print("Contact: burk.manu.2022@ksz.edu-zg.ch for support.")


if __name__ == "__main__":
    main()