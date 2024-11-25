import os
import sys
import colorama

# adds the path to the scripts folder to the system path
path_scripts = os.path.join(os.getcwd(), r"appdata\scripts")
sys.path.insert(0, path_scripts)

def access_check(): # Checks system access control and handles errors.
    try:
        import acesscontrol
        status = acesscontrol.accesscontrol()
        if status != "working":
            user_input = input("System errors detected. Start anyway? [YES / NO]: ").strip().lower()
            if user_input != "yes":
                exit()
        return status
    except Exception:
        print("Access control failed.")
        user_input = input("Start without guarantees? [YES / NO]: ").strip().lower()
        if user_input != "yes":
            exit()
        return "not working"

system_status = access_check() 

# imports the necessary modules
import log
import manager
import console
import system
import wolframalpha_module

# Setup Logger
logger = log.setup_logger(name="host")



# Main function
def main():
    try:
        logger.debug("Program started")

        system.setup_keyboard()

        # Initial setup
        global system_status
        manager.programme_started()
        system.document_writer("accesscontrol.config", "status", system_status)
        manager.print_intro()
        logger.debug("Program initialized")

        module = "calculator"
        previous_solution = None
        logger.debug("Default module set to calculator")

        module_settings = {
            "calculator": (colorama.Fore.WHITE + " ▷ Enter a calculation: ", manager.operation_assignment_module),
            "console": (colorama.Fore.LIGHTMAGENTA_EX + ">>> ", console.console),
            "wolframalpha": (colorama.Fore.LIGHTCYAN_EX + " ▷ Enter a calculation: ", wolframalpha_module.wolframalpha_query)
        }

        while True:
            answer = None
            printable, action = module_settings.get(module, module_settings["calculator"])
            logger.debug(f"Module set to {module}")
            
            user_input = input(printable).strip()

            logger.debug(f"User input: {user_input}")

            if user_input in module_settings:
                module = user_input
                logger.debug(f"Module changed to {module}")
                continue

            try:
                answer = action(user_input) if module != "calculator" else action(user_input.replace(" ",""), previous_solution)
                if answer is not None:
                    print(colorama.Fore.GREEN + str(answer))
                    previous_solution = answer
            except Exception as e:
                logger.error(f"Error in {module}: {e}")

    except Exception as e:
        print(f"Unexpected error occurred: [{e}]")
        print("Contact: burk.manu.2022@ksz.edu-zg.ch for support.")



if __name__ == "__main__":
    main()