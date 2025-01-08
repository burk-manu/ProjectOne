import os
import sys
import colorama


# adds the path to the scripts folder to the system path
path_scripts = os.path.join(os.getcwd(), r"appdata\scripts")
print(path_scripts)
sys.path.insert(0, path_scripts) # inserts the path to the scripts folder to the system path


# Setup Logger
import log
logger = log.setup_logger(name="host")


def access_check(): # Checks system access control and handles errors
    try:
        import accesscontrol
        status = accesscontrol.accesscontrol()
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
import manager
import console
import system
import wolframalpha_module


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

        module = "master math"
        previous_solution = None
        logger.debug("Default module set to master math")

        module_settings = {
            "master math": (colorama.Fore.WHITE + " (MasterMath) Enter a calculation: ", manager.operation_assignment_module),
            "console": (colorama.Fore.LIGHTMAGENTA_EX + " (Console) Enter a command:  ", console.console),
            "wolfram alpha": (colorama.Fore.LIGHTCYAN_EX + " (WolframAlpha) Enter a calculation: ", wolframalpha_module.wolframalpha_query)
        }

        while True:
            answer = None
            printable, action = module_settings.get(module, module_settings["master math"]) # gets the module settings for the current module or sets it to master math if the module is not found
            logger.debug(f"Module set to {module}")
            user_input = input(printable).strip()

            logger.debug(f"User input: {user_input}")

            if user_input in module_settings:
                module = user_input
                continue

            try:
                answer = action(user_input) if module != "master math" else action(user_input.replace(" ",""), previous_solution) # if the module is master math, the previous solution is passed as an argument
                if answer is not None:
                    print(colorama.Fore.GREEN + " ◈ " + str(answer)) # prints the answer in green
                    previous_solution = answer
            except Exception as e:
                logger.error(f"Error in {module}: {e}")

    except Exception as e:
        print(f"Unexpected error occurred: [{e}]")
        print("Contact: Project.One@gmx.ch for support.")



if __name__ == "__main__":
    main()