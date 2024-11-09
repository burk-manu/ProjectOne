import os
import colorama
import time
import json
from datetime import datetime, timedelta


import manager

date = datetime.now().date() # current date
document_name = f"{date}.log" # name of the current logfile
path = os.getcwd() # path of the 'Main.py' document
path_log_file = os.path.join(path, "appdata\log", document_name) # path of the logfile

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
            log_rotation = config.get('logfile_rotation', None)  # if config is a dictionary
        
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