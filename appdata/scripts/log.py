import os
import logging
import logging.handlers
import datetime

def setup_logger(name="host", log_dir="appdata/log", max_bytes=1024**2, backup_count=4):
    
    # create logfile name and path
    logfile_name = f"{datetime.datetime.now().strftime('%Y-%m-%d')}.{name}.log"
    path = os.getcwd()
    logfile_path = os.path.join(path, log_dir, logfile_name)

    # make directory if not exists
    os.makedirs(os.path.dirname(logfile_path), exist_ok=True)

    # create and configure logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # handler for console statements
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.WARNING)
    console_formatter = logging.Formatter("%(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)

    # handler for logfiles
    file_handler = logging.handlers.RotatingFileHandler(
        logfile_path, maxBytes=max_bytes, backupCount=backup_count
    )
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)

    # add handler to logger
    logger.addHandler(file_handler)
    if name == "host":
        logger.addHandler(console_handler)

    return logger