import os
import json
import sys
import re

import log
import system
import manager

logger = log.setup_logger(name=f"host.{__name__}")


def console(user_input):
    # define actions and expressions
    actions = {
        r"^break$": lambda: "break",
        r"^exit$": lambda: (logger.info("Process ended with user input 'exit' in console", "console"), exit()),
        r"^reset$": reset,
        r"^system info$": return_system_info,
        r"^set max int len (\d+)$": lambda: set_max_int_len(user_input[16:]),
        r"^report bug$": lambda: (system.open_link_in_browser("https://friendly-texture-b76.notion.site/13a28ff5262880faa57ed8a7d6581cf3?pvs=105"), "opening website"),
        r"^read [\w.]+, \w+$": lambda: (system.document_reader(*user_input[5:].split(", ")))

    }

    # finds the matching key and runs the action from this key
    for pattern, action in actions.items():
        if re.match(pattern, user_input):
            logger.debug("console received input from the Input Loop")
            return action()

            
    else:
        logger.info(f"console was started with an undefined command [user input: '{user_input}']")


# Console Funktionen
def return_system_info():
    path = os.getcwd()  # path of the 'Main.py' script
    with open(os.path.join(path, "appdata\system\systemdata\information.config"), 'r') as information: # path of the information.config file
        config = json.load(information)  # loads the whole document
        output = ""
        for key, value in config[0].items():
            output += f"\n{key.ljust(20)}{value}"
        return output
            

def set_max_int_len(user_input): # change the max limit of 
    sys.set_int_max_str_digits(int(user_input))
    logger.info(f"set integer max string length to {user_input} characters")


def reset():
    system.document_writer("accesscontrol.config", "status", None)
    logger.info("system resetted")
    exit()   