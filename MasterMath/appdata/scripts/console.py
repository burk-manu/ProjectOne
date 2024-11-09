import os
import json
import sys

import log
import system


def console(user_input):
    log.log_entry("console received input from the Input Loop", "console")
    if user_input == "break":
        return "break"
    
    elif user_input == "exit":
        log.log_entry("Process ended with user input 'exit' in console","console")
        exit()
    
    elif user_input == "reset":
        reset()
    
    elif user_input == "system info":
        return return_system_info()
    
    elif user_input.startswith("change log rotation "):
        return change_log_rotation(user_input)
    
    elif user_input.startswith("set max int len "):
        return set_max_int_len(user_input[16:])
            
    else:
        log.log_entry(f"console was started with an undefined command [user input: '{user_input}']", "console")
        return "command is not defined"


# Console Funktionen
def return_system_info():
    path = os.getcwd()  # path of the 'Main.py' script
    with open(os.path.join(path, "appdata\system\systemdata\information.config"), 'r') as information: # path of the information.config file
        config = json.load(information)  # loads the whole document
        output = ""
        for key, value in config[0].items():
            output += f"\n{key.ljust(20)}{value}"
        return output
            
def change_log_rotation(user_input):
    path = os.getcwd()  # path of the 'Main.py' script
    path_settings = os.path.join(path, "appdata\system\systemdata\settings.config")
    with open(path_settings, 'r') as settings: # opens doument in reading mode
        config = json.load(settings)  # loads the whole document

    if isinstance(config, list): # checks if object is a list
        config = config[0] # if so it extracts the first element of the list

    log_rotation = config.get('logfile_rotation', None) # access the correct section of the config document
    
    if log_rotation is not None:
        new_rotation = int(user_input[20:]) # user input for the new log rotation in days
        config['logfile_rotation'] = new_rotation # replace old log rotation with the new one

        with open(path_settings, 'w') as settings: # open document in writing mode to save the correct changes
            json.dump(config, settings, indent=4)  # writes new log roatation in 
            return f"logfile rotation time set to {new_rotation} days."
    else:
        return "logfile_rotation key not found in settings."

def set_max_int_len(user_input): # change the max limit of 
    sys.set_int_max_str_digits(int(user_input))
    log.log_entry(f"set integer max string length to {user_input} characters", "console")
    return f"set integer max string length to {user_input} characters"


def reset():
    system.change_accesscontrol_status(None)
    change_log_rotation(14)
    log.log_entry("system resetted", "console")
    exit()   