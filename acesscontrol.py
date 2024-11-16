import os
import json
import uuid
import platform
import log

# Define constants
SYSTEM_PATHS = [
    r"appdata/log",
    r"appdata/scripts",
    r"appdata/system",
    r"appdata/system/scientificdata",
    r"appdata/system/systemdata"
]
MODULES = [
    "sys", "os", "colorama", "time", "math", "sympy", "re", 
    "webbrowser", "datetime", "json", "shutil", "socket", "uuid", "platform"
]

# Logger setup
logger = log.setup_logger(name=f"host.{__name__}")

def get_mac_address():
    # Returns the MAC address of the device.
    return ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                     for elements in range(0, 2 * 6, 2)][::-1])

def check_access_status():
    # Checks if the system has been authorized.
    try:
        config_path = os.path.join(os.getcwd(), r"appdata/system/systemdata/accesscontrol.config")
        with open(config_path, 'r') as access_file:
            access_data = json.load(access_file)
        if (access_data.get('macadress') == get_mac_address() and
                access_data.get('status') == "working"):
            return "working"
    except Exception as e:
        logger.error(f"Access status check failed: {e}")
    return None

def check_modules():
    # Tries to import required modules and logs the result.
    problems_counted = 0
    for module in MODULES:
        try:
            __import__(module)
            logger.info(f"Successfully imported module: {module}")
        except ModuleNotFoundError:
            logger.error(f"Failed to import module: {module}")
            problems_counted += 1
    return problems_counted

def check_directories():
    # Checks if required directories exist.
    problems_counted = 0
    for path in SYSTEM_PATHS:
        full_path = os.path.join(os.getcwd(), path)
        if os.path.isdir(full_path):
            logger.info(f"Directory exists: {full_path}")
        else:
            logger.error(f"Missing directory: {full_path}")
            problems_counted += 1
    return problems_counted

def check_os():
    # Checks if the operating system is supported.
    if platform.system() == "Windows":
        logger.info("Detected Windows as the operating system.")
    else:
        logger.warning("Non-Windows OS detected. This may cause issues.")

def accesscontrol():
    # Main access control function.
    if check_access_status() == "working":
        return "working"

    logger.info("Performing full system check...")
    problems_counted = 0
    problems_counted += check_modules()
    problems_counted += check_directories()
    check_os()

    return "working" if problems_counted == 0 else "not working"