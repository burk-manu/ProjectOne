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

def change_accesscontrol_status(status):
    with open(os.path.join(os.getcwd(), r"appdata\system\systemdata\accesscontrol.config"), 'r') as accesscontrol_document:
        accesscontrol_status = json.load(accesscontrol_document)
        accesscontrol_status['status'] = status
        accesscontrol_status['macadress'] = get_mac_adress()
           
    with open(os.path.join(os.getcwd(), r"appdata\system\systemdata\accesscontrol.config"), 'w') as accesscontrol_document:
        json.dump(accesscontrol_status, accesscontrol_document, indent=4)
        
        log.log_entry(f"accesscontrol status and hostname changed successfully to status: '{status}' and hostname: '{get_mac_adress()}'", "system")
        return f"accesscontrol status successfully changed to {status}"
        