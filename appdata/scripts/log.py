import os
import logging
import logging.handlers
from colorama import Fore, Style, init

# Initialisiere colorama
init(autoreset=True)

class ColoredFormatter(logging.Formatter): # [AI]
    # define color for different log levels
    COLORS = {
        "DEBUG": Style.DIM + Fore.CYAN,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Style.BRIGHT + Fore.RED
    }

    def format(self, record):
        # add colors to the corresponding log levels
        color = self.COLORS.get(record.levelname, "") # get color for log level
        reset = Style.RESET_ALL # reset style
        record.msg = f"{color}{record.msg}{reset}" # add color to message
        return super().format(record)

def setup_logger(name="host", log_dir="appdata/log", max_bytes=1024*8, backup_count=4):
    logfile_name = f"Log-{name}.log"
    path = os.getcwd()
    logfile_path = os.path.join(path, log_dir, logfile_name)

    os.makedirs(os.path.dirname(logfile_path), exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if name == "host":
        file_handler = logging.handlers.RotatingFileHandler(logfile_path, maxBytes=1024*64, backupCount=backup_count)
    else:
        file_handler = logging.handlers.RotatingFileHandler(logfile_path, maxBytes=max_bytes, backupCount=1)

    file_formatter = logging.Formatter(
        "%(asctime)s - %(filename)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)
    file_handler.stream.reconfigure(encoding='utf-8')

    logger.addHandler(file_handler)

    if name == "host":
        logfile_path_2 = os.path.join(path, log_dir, "longtimeLogs", logfile_name)
        os.makedirs(os.path.dirname(logfile_path_2), exist_ok=True)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Verwende die farbige Formatter
        console_formatter = ColoredFormatter("%(levelname)s - %(message)s")
        console_handler.setFormatter(console_formatter)
        console_handler.stream.reconfigure(encoding='utf-8')

        file_handler_2 = logging.handlers.RotatingFileHandler(
            logfile_path_2, maxBytes=1024*2, backupCount=8
        )
        file_formatter_2 = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler_2.setFormatter(file_formatter_2)
        file_handler_2.setLevel(logging.WARNING)
        file_handler_2.stream.reconfigure(encoding='utf-8')

        logger.addHandler(console_handler)
        logger.addHandler(file_handler_2)

    return logger