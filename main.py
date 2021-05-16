# -*- coding: utf-8 -*-
# Author : DSWEB19778
# Version : 4.0
# Title : Apple ID checker
# Date : 2021
# Donate : https://paypal.me/wecandoittogheter
# Thanks to : God First & me
# Note : This Just an update for old script this will make it stable and faster
# Make sure to update keys every week

from inc.api import *
from time import sleep
import threading


clear(system_eck())  # Clean Command
print(logo("DSWEB19778", time.asctime(), "4.0",
      "APPLE-API", "https://paypal.me/wecandoittogheter"))  # Logo COpyRights


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

        delay = 0
        for fr in op:
            
            x = fr.strip("\n")
            delay += 1
            if delay == 20:
                sleep(10)
                print(blue+"    [+] ------------- Waiting -------------")
                delay = 0
                continue
            else:
                pass
            t = threading.Thread(target=apple_api, args=(x,))
            t.start()
            

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
