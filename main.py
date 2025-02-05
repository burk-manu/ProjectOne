import os
import sys
import colorama

# Initialize Colorama for colored terminal output
colorama.init(autoreset=True)

# Determine the script's base directory reliably and add scripts folder to sys.path
base_dir = os.path.dirname(os.path.abspath(__file__))
path_scripts = os.path.join(base_dir, "appdata", "scripts")
sys.path.insert(0, path_scripts)

# Setup Logger
import log
logger = log.setup_logger(name="host")

def access_check() -> str:
    """
    Checks system access control and handles errors.
    
    Returns:
        A string indicating the status of the access control.
    """
    try:
        import accesscontrol
        status = accesscontrol.accesscontrol()
        if status != "working":
            user_input = input("System errors detected. Start anyway? [YES / NO]: ").strip().lower()
            if user_input != "yes":
                sys.exit(1)
        return status

    except Exception:
        logger.warning("Access control failed.", exc_info=True)
        user_input = input("Start without guarantees? [YES / NO]: ").strip().lower()
        if user_input != "yes":
            sys.exit(1)
        return "not working"

# Execute access check before importing other modules if necessary
system_status = access_check()

# Import the necessary modules after initial checks
import manager
import console
import system
import wolframalpha_module

def main() -> None:
    """
    Main entry point of the program. Sets up the system, handles user input,
    and delegates commands to the appropriate module.
    """
    try:
        logger.debug("Program started")
        system.setup_keyboard()

        # Initial setup
        manager.programme_started()
        system.document_writer("accesscontrol.config", "status", system_status)
        manager.print_intro()
        logger.debug("Program initialized")

        # Default module configuration
        current_module = "master math"
        previous_solution = None
        logger.debug("Default module set to master math")

        # Mapping of module names to their prompt and handler function.
        module_settings = {
            "master math": (
                colorama.Fore.WHITE + " (MasterMath) Enter a calculation: ",
                lambda user_input: manager.operation_assignment_module(user_input.replace(" ", ""), previous_solution)
            ),
            "console": (
                colorama.Fore.LIGHTMAGENTA_EX + " (Console) Enter a command: ",
                console.console
            ),
            "wolfram alpha": (
                colorama.Fore.LIGHTCYAN_EX + " (WolframAlpha) Enter a calculation: ",
                wolframalpha_module.wolframalpha_query
            )
        }

        # Main input loop
        while True:
            prompt, action = module_settings.get(current_module, module_settings["master math"])
            logger.debug(f"Module set to {current_module}")

            user_input = input(prompt).strip().lower()
            logger.debug(f"User input: {user_input}")

            # Allow user to change module or exit the program gracefully
            if user_input in module_settings:
                current_module = user_input
                continue
            elif user_input in {"exit", "quit"}:
                logger.info("User requested to exit the program.")
                break

            try:
                answer = action(user_input)

                if answer is not None:
                    print(colorama.Fore.GREEN + " ◈ " + str(answer))
                    previous_solution = answer

            except Exception as e:
                logger.exception(f"Error in module '{current_module}': {e}")

    except Exception as e:
        logger.exception(f"Unexpected error occurred: {e}")
        print(f"Unexpected error occurred: [{e}]")
        print("Contact: Project.One@gmx.ch for support.")
        sys.exit(1)

if __name__ == "__main__":
    main()