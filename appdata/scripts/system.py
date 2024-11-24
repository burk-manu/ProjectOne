import os
import sys
import json
import uuid
import platform
import webbrowser
import keyboard

import log

logger = log.setup_logger(name=f"host.{__name__}") # setup logger

def get_mac_adress(): # returns the mac adress [AI]
    mac_adress = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    return mac_adress

def get_operating_system(): # returns the operating system
    return platform.system()

def file_exists(path): # checks if a file exists
    return os.path.exists(path)
    
def document_writer(document_name, key, value, path=os.path.join(os.getcwd(), r"appdata\system\systemdata"), element=0): # writes data into a document
    directory_path = path
    document_path = os.path.join(directory_path, document_name)
    if os.path.exists(document_path):
        with open (document_path, 'r') as document_json:
            document = json.load(document_json)
            if isinstance(document, list):
                document = document[element]
            
            if isinstance(document, dict):
                document[key] = value
        
        with open (document_path, 'w') as document_json:
            json.dump(document, document_json, indent=4)
        
        return f"successfully set {key} from document {document_name} to {value}"
    else:
        return f"document {document_name} couldn't be found in directory '{directory_path}'"

    
def document_reader(document_name, key, element=0): # reads information from a document
    document_path = os.path.join(os.getcwd(), r"appdata\system\systemdata",document_name)
    if file_exists(document_path):
        with open (document_path, 'r') as document_json:
            document = json.load(document_json)
            if isinstance(document, list):
                document = document[element]
            if isinstance(document, dict):
                value = document[key]
                return value
    else:
        return f"couldn't find File {document_name} in 'appdata\system\systemdata'"

def create_file(name, path=(os.path.join(os.getcwd(), r"appdata\system\systemdata"))): # creates a file
    if os.path.exists(os.path.join(path, name), 'w'):
        return "File already exists"
    with open(os.path.join(path, name), 'w'):
        return f"File {name} successfully created"
    
    
def remove_file(path): # removes a file
    if os.path.exists(path):
        os.remove(path)
    else:
        return "File/directory {path} doesn't exist"
    
def reset(): # resets the system
    document_writer("accesscontrol.config", "status", None)
    logger.info("system resetted")
    exit()

def return_system_info(): # returns system information
    path = os.getcwd()  # path of the 'Main.py' script
    with open(os.path.join(path, "appdata\system\systemdata\information.config"), 'r') as information: # path of the information.config file
        config = json.load(information)  # loads the whole document
        output = ""
        for key, value in config[0].items():
            output += f"\n{key.ljust(20)}{value}"
        return output

def set_max_int_len(user_input): # changes the maximum integer length
    sys.set_int_max_str_digits(int(user_input))
    logger.debug(f"set integer max string length to {user_input} characters")
    return f"set integer max string length to {user_input} characters"

def open_link_in_browser(url): # opens a specific URL in the browser
    webbrowser.open(url)
    logger.info(f"opening website with url: {url}")
    return "opening website . . . "

def setup_keyboard(): # sets up the shortcuts for the program
    keyboard.add_hotkey('f1', lambda: open_link_in_browser("https://eduzg-my.sharepoint.com/:f:/g/personal/burk_manu_2022_ksz_edu-zg_ch/EviqcQd93dJOv9hP0eUGdMkBBppDHHHLWhCKwl_MPkYbLg?e=vY0rQG"))