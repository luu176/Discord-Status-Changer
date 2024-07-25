import requests 
import time
import json
from colorama import Fore
import os


banner = f"""{Fore.CYAN}

░██████╗████████╗░█████╗░████████╗██╗░░░██╗░██████╗  ░█████╗░██╗░░██╗░█████╗░███╗░░██╗░██████╗░███████╗██████╗░
██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║░░░██║██╔════╝  ██╔══██╗██║░░██║██╔══██╗████╗░██║██╔════╝░██╔════╝██╔══██╗
╚█████╗░░░░██║░░░███████║░░░██║░░░██║░░░██║╚█████╗░  ██║░░╚═╝███████║███████║██╔██╗██║██║░░██╗░█████╗░░██████╔╝
░╚═══██╗░░░██║░░░██╔══██║░░░██║░░░██║░░░██║░╚═══██╗  ██║░░██╗██╔══██║██╔══██║██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗
██████╔╝░░░██║░░░██║░░██║░░░██║░░░╚██████╔╝██████╔╝  ╚█████╔╝██║░░██║██║░░██║██║░╚███║╚██████╔╝███████╗██║░░██║
╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═════╝░  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝

Coded by luu_1 
.gg/developers     

      """
print(banner)
token = input(f"{Fore.WHITE}Input your token: ")
header = {
        'Authorization': token
}
token_check = requests.get("https://discord.com/api/v9/users/@me", headers=header)
if token_check.status_code != 200:
    print(f"{Fore.RED}[-] INVALID TOKEN{Fore.WHITE}")
    exit()
os.system('cls||clear')
print(banner)
user = token_check.json()['username']
status = []
x = True
while x:
    try:
        print(f"{Fore.WHITE}Enter number of status's: ")
        num = int(input(f"{Fore.LIGHTGREEN_EX}{user}@devbase:~$ "))
        x = False
    except ValueError:
        os.system('cls||clear')
        print(banner)
        print(f"{Fore.LIGHTGREEN_EX}{user}@devbase:~$ {Fore.RED}Has to be a number. {Fore.WHITE}")

for i in range(num):
    os.system('cls||clear')
    print(banner)
    print(f"{Fore.WHITE}Enter status #{i+1}:")
    statuss = input(f"{Fore.LIGHTGREEN_EX}{user}@devbase:~$ ")
    status.append(statuss)

current_status = requests.get("https://discord.com/api/v10/users/@me/settings", headers=header).json()

while True:
    for i in range(num):
        current_status['custom_status']['text'] = status[i]
        json = {
                "custom_status": current_status['custom_status'],
            }
        r= requests.patch("https://discord.com/api/v10/users/@me/settings", headers=header, json=json)
        if r.status_code == 200:
            os.system('cls||clear')
            print(banner)
            print(f'{Fore.LIGHTGREEN_EX}{user}@devbase:~$ ')
            print(f"{Fore.WHITE}[+] Set status to --> {status[i]} {Fore.WHITE}")
        else:
            os.system('cls||clear')
            print(banner)
            print(f'{Fore.LIGHTGREEN_EX}{user}@devbase:~$ ')
            print('{Fore.RED}[-] Error setting status:', r.json(), f'{Fore.WHITE}')
        time.sleep(1.5)
