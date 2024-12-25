import os
import logging
import logging.handlers


def setup_logger(name="host", log_dir="appdata/log", max_bytes=1024*32, backup_count=4): # function to setup loggers [AI]
    
    # create logfile name and path
    logfile_name = f"Log-{name}.log"
    path = os.getcwd()
    logfile_path = os.path.join(path, log_dir, logfile_name)

    # make directory if not exists
    os.makedirs(os.path.dirname(logfile_path), exist_ok=True)

    # create and configure logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # detailed handler for logfiles
    if name == "host":
        file_handler = logging.handlers.RotatingFileHandler(logfile_path, maxBytes=1024*256, backupCount=backup_count)
    else:
        file_handler = logging.handlers.RotatingFileHandler(logfile_path, maxBytes=max_bytes, backupCount=1)

    file_formatter = logging.Formatter(
        "%(asctime)s - %(filename)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)
    file_handler.stream.reconfigure(encoding='utf-8')

    # add Handler to logger
    logger.addHandler(file_handler)


    if name == "host": #special handler for the main logger

        logfile_path_2 = os.path.join(path, log_dir, "longtimeLogs", logfile_name)
        os.makedirs(os.path.dirname(logfile_path_2), exist_ok=True)

        # handler for console statements
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_formatter = logging.Formatter("%(levelname)s - %(message)s")
        console_handler.setFormatter(console_formatter)
        console_handler.stream.reconfigure(encoding='utf-8')

        # less detailed handler for logfiles
        file_handler_2 = logging.handlers.RotatingFileHandler(
            logfile_path_2, maxBytes=max_bytes, backupCount=2
        )
        file_formatter_2 = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler_2.setFormatter(file_formatter_2)
        file_handler_2.setLevel(logging.WARNING)
        file_handler_2.stream.reconfigure(encoding='utf-8')

        # add handler to logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler_2)

    return logger