# - Import library
try:

    import requests as req
    import re
    import json
    import url_parser
    import fake_useragent as gagent
    import colorama as c
    import os
    import platform as pl
    import time
    import sys
    import random as h
    from urllib3.exceptions import InsecureRequestWarning
    req.packages.urllib3.disable_warnings(InsecureRequestWarning) # Disable SSL Warning

except ImportError as imerr:

    print("Library Error Please install all important library")
    exit()

# Set colors
red = c.Fore.LIGHTRED_EX
green = c.Fore.LIGHTGREEN_EX
yellow = c.Fore.LIGHTYELLOW_EX
genta = c.Fore.LIGHTMAGENTA_EX
blue = c.Fore.LIGHTBLUE_EX
yell = c.Fore.YELLOW


def fakeagent(browser_name):  # generate a fake user agent for headers

    ag = gagent.FakeUserAgent(
        cache=True, use_cache_server=True, verify_ssl=True)
    if browser_name == "chrome":
        user = ag.chrome
    elif browser_name == "firefox":
        user = ag.firefox
        return user


def ison(site, state):  # Check if the server is online
    try:
        mainsite = url_parser.get_base_url(site)
        con = req.get(mainsite).status_code
        if con == int(state):
            return True
        else:
            return False
    except IOError as err:
        print("    # - Target IS dead")


def rzlt_folder(): # Check if rzlt folder exist or not and make one 
    ospath = os.path
    folder = "rzlt"
    if ospath.isdir(folder) == True:
        return True
    else:
        os.mkdir(folder)
        return False


def system_eck():  # detect your oprating system and check if supported for this script

    myOs = pl.system()
    required_system = ["Windows", "Mac", "Linux"]
    for plat in required_system:
        if plat in myOs:
            return {"supported": True, "name": myOs}
        elif plat == None:
            return {"supported": False, "name": "Undefined"}


def clear(system):  # smart cleaning for all platfrom
    commands = {
        "linux": "clear",
        "windows": "cls",
        "mac": "clear"
    }
    if (system['supported'] == True and system['name'] == "Linux" or system['name'] == "Mac"):
        return os.system(commands['linux'])
    elif (system['supported'] == True and system['name'] == "Windows"):
        return os.system(commands['windows'])
    else:
        return False
        exit()


def logo(author, date, version, title,ppid):  # logo
    
    logoo = """
    
     █████╗ ██████╗ ██████╗ ██╗     ███████╗    ██╗  ██╗ █████╗ ████████╗
    ██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝    ██║  ██║██╔══██╗╚══██╔══╝
    ███████║██████╔╝██████╔╝██║     █████╗█████╗███████║███████║   ██║   
    ██╔══██║██╔═══╝ ██╔═══╝ ██║     ██╔══╝╚════╝██╔══██║██╔══██║   ██║   
    ██║  ██║██║     ██║     ███████╗███████╗    ██║  ██║██║  ██║   ██║   
    ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                            
    #! -Author : """+str(author)+"""
    #! -Date : """+str(date)+"""
    #! -Version : """+str(version)+"""
    #! -Title : """+str(title)+"""
    #! -Donate : """+str(ppid)+"""
    #! -Warning : """+red+""" IDMSA Is an old Exploit It can be Limited
    """

    return logoo
    
