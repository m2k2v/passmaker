try :
    import colorama
except : 
    print("colorama is nat install in your divice. you can install that ذy typing the command : pip install colorama")
import colorama
import time
import os
import sys
from colorama import init
import random
init()

###  CODES
# clear 
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# banner
def banner():
    print(colorama.Fore.RED + """
    
     ╔═══════════════════════════════════════════════════╗ 
     ║   ███╗   ███╗██████╗ ██╗  ██╗██████╗ ██╗   ██╗    ║
     ║   ████╗ ████║╚════██╗██║ ██╔╝╚════██╗██║   ██║    ║
     ║   ██╔████╔██║ █████╔╝█████╔╝  █████╔╝██║   ██║    ║
     ║   ██║╚██╔╝██║██╔═══╝ ██╔═██╗ ██╔═══╝ ╚██╗ ██╔╝    ║
     ║   ██║ ╚═╝ ██║███████╗██║  ██╗███████╗ ╚████╔╝     ║
     ║   ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝  ╚═══╝      ║
     ║                                                   ║
     ║═══════════════════════════════════════════════════║
     ║                                                   ║
     ║        FOLLOW ME ON INSTAGRAM : @M2K2V            ║
     ║                                                   ║
     ╚═══════════════════════════════════════════════════╝
    
    """)

# MENU 
def menu():
    time.sleep(0.5)
    print(colorama.Fore.RED + " [►]" + colorama.Fore.WHITE + "M2K2V"+ colorama.Fore.GREEN + "/" + colorama.Fore.WHITE +"PASSMAKER"+ colorama.Fore.GREEN + "/" + colorama.Fore.YELLOW + "HOME")
    time.sleep(0.5)
    print(colorama.Fore.RED + " 1)" + colorama.Fore.CYAN + "PASSMAKER")
    time.sleep(0.5)
    print(colorama.Fore.RED + " 2)" + colorama.Fore.CYAN + "Exit")
    time.sleep(0.5)
    anwer = input(colorama.Fore.GREEN + " Enter part number >>> ")
    if anwer == "1" : 
        makepass()
    elif anwer == "2" : 
        Exit()
    else : 
        time.sleep(0.5)
        print(colorama.Fore.RED + "/n [!]" + colorama.Fore.YELLOW + "ERROR : " + colorama.Fore.GREEN + "Please enter a valid number")
        time.sleep(1.5)
        RUN()

# make pass
def makepass() :
    password = ""
    abc = open("abc.txt" , "r").read()
    abc = abc.split("\n")
    len = int(input(colorama.Fore.GREEN + "\n How long do you want the password to be? >>>  "))
    for x in range (len):
        temp = random.sample(abc ,1)
        password += str(temp[0])
        temp = ""
    print(colorama.Fore.RED + "\n [" + colorama.Fore.GREEN + "►" + colorama.Fore.RED + "]" +  colorama.Fore.GREEN + "Your password is >>> " + colorama.Fore.WHITE + password)
    time.sleep(2)
    input(colorama.Fore.CYAN + "\n You can coppy this password :)) --- press Enter to Continue >>>  ")
    RUN()

# Exit 
def Exit():
    print(colorama.Fore.YELLOW + "\n Good Luck :))) ")
    time.sleep(2)
    sys.exit(0)


### RUN 
def RUN():
    clear()
    banner()
    menu()
RUN()