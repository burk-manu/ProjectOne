import sys
import shutil
import os
import socket
import json
import uuid
import platform
import webbrowser

import log

logger = log.setup_logger(name=f"host.{__name__}")

def get_mac_adress(): # returns the mac adress [AI]
    mac_adress = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    return mac_adress

def get_operating_system(): # retunrns the operatings system
    return platform.system()

def file_exists(path):
    return os.path.exists(path)
    
def document_writer(document_name, key, value, element=0):
    directory_path = os.path.join(os.getcwd(), r"appdata\system\systemdata")
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

    
def document_reader(document_name, key, element=0):
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

def create_file(name, path=(os.path.join(os.getcwd(), r"appdata\system\systemdata"))):
    if os.path.exists(os.path.join(path, name), 'w'):
        return "File already exists"
    with open(os.path.join(path, name), 'w'):
        return f"File {name} successfully created"
    
    
def remove_file(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        return "File/directory {path} doesn't exist"


def open_link_in_browser(url): # opens a specific URL in the browser
    webbrowser.open(url)
    logger.info(f"opening website with url: {url}")
    return "opening website . . . "