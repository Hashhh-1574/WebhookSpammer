import requests
import time
import msvcrt
import os
from colorama import init, Fore
from os import system

os.system("title Webhook Exploiter")

print(Fore.RED + "Executing Spammer.")
time.sleep(1)
print(Fore.RED + "Executing Spammer..")
time.sleep(1)
print(Fore.RED + "Executing Spammer...")
time.sleep(1)
print(Fore.RED + "Executing Spammer....")
time.sleep(1)
print(Fore.RED + "Executing Spammer.....")
time.sleep(1)
print(Fore.RED + "Executing Spammer......")
time.sleep(1)

banner = (Fore.MAGENTA + """
  ||
  ||_________________________/'|
 _| O======/                   |
|_|              ============  |
  |  __  ______________________|
  |_/  )(     |___||     O-   /
      (  )    /  / |_________/
      (  )   /  /    | ) |   |      Uzi Spammer
      (__)  /  /     \___|__(       By: https://github.com/Hashhh-1574
           /  /          )   \
          /  /            )   \
         /  /              )___\
        /  /
       /__/""")
x = 1
print(banner)

WEBHOOK_URL = str(input("\n\nWebhook URL: "))
WEBHOOK_USERNAME = str(input("\nWebhook NickName:: "))
WEBHOOK_AVATAR = str(input("\nAvatar:  "))
WEBHOOK_CONTENT = str(input("\nMessage "))
SPAM = int(input("\nHow Many Messages (Limit of 30) "))

while x < SPAM:
    try:
        payload = {"content":WEBHOOK_CONTENT,"username":WEBHOOK_USERNAME,"avatar_url":WEBHOOK_AVATAR}
        r = requests.post(WEBHOOK_URL,data=payload)
        x +=1
        print("[+] Webhook Spamming")
    except:
        print("[-] Eror")
        pass
print("\n[+] Spam Done ")
