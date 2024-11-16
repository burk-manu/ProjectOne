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


"""

# code to delete

import os
import colorama
import time
import json
from datetime import datetime, timedelta

import manager
import system

date = datetime.now().date() # current date
document_name = f"{date}.log" # name of the current logfile
path = os.getcwd() # path of the 'Main.py' document
path_log_file = os.path.join(path, "appdata\log", document_name) # path of the logfile

if not os.path.isdir(os.path.join(path, "appdata\log")):
    os.makedirs(os.path.join(path, "appdata\log"))

def create_logfile():
    if not system.file_exists(path, document_name):
        with open(path_log_file, 'w') as document: # öffnet das Log-File
            programm_version = system.document_reader("information.config", "Version")
            document.write(f"running Master Math version: {programm_version}")

def error(error, module, code):
    date = datetime.now().strftime("%d.%m.%Y %H:%M:%S") # Setzt die Variable date auf das aktuelle Datum und die Aktuelle Uhrzeit ohne Kommastellen der Sekunden
    with open(path_log_file, 'a') as document: # öffnet das Log-File
        document.write('\n' f"[ERROR]		[{date}]	[{module}] {error} (Error-Code: {code})") # Fügt dem Logfile einen ERROR-Eintrag hinzu
    return colorama.Fore.RED + f" -> ERROR: {error}" # Gibt die formatierte Error-Meldung zurück für die Ausgabe auf der Konsole

def log_entry(entry, module):
    date = datetime.now().strftime("%d.%m.%Y %H:%M:%S") # Setzt die Variable date auf das aktuelle Datum und die Aktuelle Uhrzeit ohne Kommastellen der Sekunden
    with open(path_log_file, 'a') as document: # öffnet das Log-File
        document.write('\n' f"[Information]	[{date}]	[{module}] {entry}") # Fügt dem Logfile einen Informations-Eintrag hinzu
    return f"Information: {entry}"

def delete_old_logs():
    directory = os.path.join(path, "appdata\log") # open logfile directory
    with open(os.path.join(path, "appdata\system\systemdata\settings.config"), 'r') as settings:
        config = json.load(settings)
        if isinstance(config, list):
            log_rotation = config[0].get('logfile_rotation', None)  # if config is a list get the first element
        else:
            log_rotation = config.get('logfile_rotation', None)  # if config is anything esle (in this case a dictionary)
        
        if log_rotation is None:
            print(error("logfile_rotation key not found in settings", "Delete Old Logfiles", "X103"))
            return
    
    try:
        if not os.path.isdir(directory): # check if directory exists
            return f"The directory {directory} does not exist"
        
        rotation_days = int(log_rotation) # calculate the date of logfile rotation
        cutoff_date = datetime.now() - timedelta(days=rotation_days)
        
        # Durchlaufe alle Dateien im angegebenen Verzeichnis
        for filename in os.listdir(directory): # check for every document in the specified directory
            file_path = os.path.join(directory, filename) # join the path of the directory and the filename
            
            if os.path.isfile(file_path): # check if it is a document
                try:
                    date_str = filename.replace('.log', '') # extract the date from the name of the logfile
                    
                    file_date = datetime.strptime(date_str, '%Y-%m-%d') # check if date format is YYYY-MM-DD
                    
                    if file_date < cutoff_date: # compare file date with cutoff date
                        os.remove(file_path) # if the logfile is too old it gets deleted
                        print(f"{filename} got deleted, because it is older than {rotation_days} days")
                        
                except ValueError:
                    print(error("Invalid logfile date format. Manual deletion may be required.", "logfile manager", "X101")) # Incorrect date formatting
    
    except Exception as e:
        print(error("Something unexpected went wrong.", "logfile manager", "X102"))



def change_log_rotation(user_input):
    system.document_writer("settings.config", "logfile_rotation", int(user_input))


    path = os.getcwd()  # path of the 'Main.py' script
    path_settings = os.path.join(path, "appdata\system\systemdata\settings.config")
    with open(path_settings, 'r') as settings: # opens doument in reading mode
        config = json.load(settings)  # loads the whole document

    if isinstance(config, list): # checks if object is a list
        config = config[0] # if so it extracts the first element of the list

    log_rotation = config.get('logfile_rotation', None) # access the correct section of the config document
    
    if log_rotation is not None:
        new_rotation = int(user_input) # user input for the new log rotation in days
        config['logfile_rotation'] = new_rotation # replace old log rotation with the new one

        with open(path_settings, 'w') as settings: # open document in writing mode to save the correct changes
            json.dump(config, settings, indent=4)  # writes new log roatation in 
            return f"logfile rotation time set to {new_rotation} days."
    else:
        return "logfile_rotation key not found in settings."
"""