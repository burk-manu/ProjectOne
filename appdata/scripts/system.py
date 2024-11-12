import sys
import shutil
import os
import socket
import json
import uuid
import platform

import log

def get_mac_adress():
    mac_adress = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
    return mac_adress

def get_operating_system():
    return platform.system()

def document_writer(document_name, key, value):
    document_path = os.path.join(os.getcwd(), r"appdata\system\systemdata",document_name)
    with open (document_path, 'r') as document_json:
        document = json.load(document_json)
        document[key] = value
    
    with open (document_path, 'w') as document_json:
        json.dump(document, document_json, indent=4)

    
    
def document_reader(document_name, key):
    document_path = os.path.join(os.getcwd(), r"appdata\system\systemdata",document_name)
    with open (document_path, 'r') as document_json:
        document = json.load(document_json)
        value = document[key]
        return value


def change_accesscontrol_file(key, value):
    with open(os.path.join(os.getcwd(), r"appdata\system\systemdata\accesscontrol.config"), 'r') as accesscontrol_document:
        accesscontrol_status = json.load(accesscontrol_document)
        if key in accesscontrol_status:
            accesscontrol_status[key] = value
            return f"information {key} in accesscontrol.config changed to {value}"
        else :
            return f"in the dictionary accesscontrol.config doesn't exist a key {key}"
           
    with open(os.path.join(os.getcwd(), r"appdata\system\systemdata\accesscontrol.config"), 'w') as accesscontrol_document:
        json.dump(accesscontrol_status, accesscontrol_document, indent=4)
        
        log.log_entry(f"accesscontrol status and hostname changed successfully to status: '{status}' and hostname: '{get_mac_adress()}'", "system")
        return f"accesscontrol status successfully changed to {status}"
        