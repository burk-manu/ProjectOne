# checks if there could be any problems to start the programm
def access_check():
    try:
        import acesscontrol
        status = acesscontrol.accesscontrol()

        if status == "working":
            pass
        elif status == "not working":
            user_input = input("The system has reported one or more errors. You can start the programme, but this will probably cause an error. Do you want to continue [YES / NO]? ")
            if user_input.lower() == "no":
                exit()
                
        else:
            status = "not working"

        return status
            
    except Exception:
        print("there is a problem with the acesscontrol function.")
        user_input = input("You can start the programme, but we can not guarantee that it will run. Do you want to continue [YES / NO]?")
        if  user_input.lower() == "no":
            exit()



# programm begins
try:
    
    system_status = access_check()

    import sys
    import os
    import colorama
    import time

    # needed to import the other scripts
    path = os.getcwd() # get path of the Main.py script
    path_scripts = os.path.join(path, "appdata\scripts") # refers to the subfolder ‘scripts’
    sys.path.insert(0, path_scripts) # adds path to the sys.path list where pythen checks for files to import
    
    sys.set_int_max_str_digits(4300)

    # importing functions
    import manager
    import log
    import console
    import system

    system.document_writer("accesscontrol.config", "status", system_status)

    # programm starts
    manager.programm_started() # activates the function "programm_started"

    manager.print_intro() # prints out the intro
    log.log_entry("Programm started and function 'print_intro' started","Intro print command") # logfile entry


    previous_solution = None

    while True:
        user_input = input(colorama.Fore.WHITE + "▷ Enter a calculation: ")
        if user_input != "console":
            solution = manager.operation_assignment_module(user_input, previous_solution) # asks for an Input and forwards it to the OAM
            log.log_entry(f"received response from Operation Assignment Module [response: {solution}]", "Input Loop") # logfile entry
            print(colorama.Fore.GREEN + str(solution)) # prints the solution
            log.log_entry("printed response from Operation Assignment Module: task excecuted", "Input Loop") # logfile entry
            if "ERROR" not in str(solution): # checks if previous output was an error
                previous_solution = solution # if not, 'last_solution' get set to the previous output
        else: # opens the programme's own console
            print(colorama.Fore.LIGHTMAGENTA_EX + "console started . . .")
            log.log_entry("Console started", "Input Loop")
            while True: # continues to prompt for input
                printable = console.console(input(colorama.Fore.LIGHTMAGENTA_EX + "▢ Enter a command: "))
                if printable == "break": # if input is 'close' console will be stopped
                    print(colorama.Fore.LIGHTMAGENTA_EX + "console stopped")
                    log.log_entry("Console stopped by 'break'", "Input Loop")
                    break # stoppt die Schleife
                else:
                    print(colorama.Fore.LIGHTMAGENTA_EX + "▸",printable) # prints out the returen of the console

except ZeroDivisionError as e:
        print("Sorry! Something unexpected went wrong...", f"[{e}]")
print("Contact the developer at burk.manu.2022@ksz.edu-zg.ch | The bug will be fixed as soon as possible.") # prints an error for an unexpected error
input("press enter to open Wolframalpha")
manager.open_link_in_browser("Wolframalpha.com")