systempaths = [r"appdata\log", r"appdata\scripts", r"appdata\system", r"appdata\system\scientificdata", r"appdata\system\systemdata"]
modules = ["sys", "os", "colorama", "time", "math", "sympy", "re", "webbrowser", "datetime","json","shutil", "socket", "uuid", "platform"]

successfully_imported_modules = {}

def accesscontrol():
    # checks if this device is already checked
    problems_counted = 0
    try:
        import os
        import json
        import socket
        import uuid
        import platform
        mac_adress = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])
        with open(os.path.join(os.getcwd(), r"appdata\system\systemdata\accesscontrol.config"), 'r') as accesscontrol_document:
            accesscontrol_status = json.load(accesscontrol_document)
            if accesscontrol_status['macadress'] == mac_adress and accesscontrol_status['status'] == "working":
                return accesscontrol_status['status']
    except Exception:
        pass
    
    # checks if everything is prepared for the programm to install (Plug-Ins, operating system, python version, etc.)
    try:
        
        for module in modules:
            try:
                importing_module = __import__(module)
                successfully_imported_modules[module] = importing_module
                print(f"successfully imported module {module}")
            except ModuleNotFoundError:
                print(f"couldn't import module '{module}'; make sure you installed it")
                problems_counted += 1
            
        input("Press return to continue checking...")
        
        path = os.getcwd() # path of the 'Main.py' script
        for systempath in systempaths:
            directory = os.path.join(path, systempath)
            print(f"found directory: {directory}")
            if not os.path.isdir(directory):
                print(f"programm couldn't find the directory {directory}")
                problems_counted += 1
        
        input("Press return to continue checking...")
        
        try:
            import platform
            if platform.system() == "Windows":
                print("detected windows as your operating system")
            else:
                print("looks like you're no using windows as your operating system; This may causes errors")
        except Exception:
            pass
        
        input("Press return to continue checking...")
        
    except Exception:
        pass
    
    if problems_counted == 0:
        return "working"
    else:
        return "not working"