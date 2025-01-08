import re

import log
import system

logger = log.setup_logger(name=f"host.{__name__}") # setup logger


def console(user_input): # console function
    logger.debug("Console started")
    # define actions and expressions
    actions = {
        r"^exit$": lambda: (logger.info("Process ended with user input 'exit' in console"), exit()),
        r"^reset$": lambda: system.reset(),
        r"^system info$": lambda: system.return_system_info(),
        r"^system status$": lambda: system.return_system_status(),
        r"^set max int len (\d+)$": lambda: system.set_max_int_len(user_input[16:]),
        r"^report bug$": lambda: system.open_link_in_browser("https://friendly-texture-b76.notion.site/13a28ff5262880faa57ed8a7d6581cf3?pvs=105"),
        r"^read [\w.]+, [ \w]+$": lambda: (system.document_reader(*user_input[5:].split(", "))),
        r"^clear$": lambda: system.clear_console()
    }

    # finds the matching key and runs the action from this key
    for pattern, action in actions.items():
        if re.match(pattern, user_input):
            logger.debug("console received input from the Input Loop")
            return action()

            
    else:
        logger.info(f"console was started with an undefined command [user input: '{user_input}']")