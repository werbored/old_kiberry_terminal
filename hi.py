from colorama import Fore, Back, init
from os import name, system, get_terminal_size
from time import sleep

blue = Fore.BLUE
green = Fore.LIGHTGREEN_EX

ascii1 = blue+" ██ ▄█▀ ██▓ ▄▄▄▄   ▓█████  ██▀███   ██▀███ ▓██   ██▓ "+green+"   ▄████▄   ███▄ ▄███▓▓█████▄ "
ascii2 = blue+" ██▄█▒ ▓██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒▓██ ▒ ██▒▒██  ██▒ "+green+"  ▒██▀ ▀█  ▓██▒▀█▀ ██▒▒██▀ ██▌"
ascii3 = blue+"▓███▄░ ▒██▒▒██▒ ▄██▒███   ▓██ ░▄█ ▒▓██ ░▄█ ▒ ▒██ ██░ "+green+"  ▒▓█    ▄ ▓██    ▓██░░██   █▌"
ascii4 = blue+"▓██ █▄ ░██░▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  ▒██▀▀█▄   ░ ▐██▓░ "+green+"  ▒▓▓▄ ▄██▒▒██    ▒██ ░▓█▄   ▌"
ascii5 = blue+"▒██▒ █▄░██░░▓█  ▀█▓░▒████▒░██▓ ▒██▒░██▓ ▒██▒ ░ ██▒▓░ "+green+"  ▒ ▓███▀ ░▒██▒   ░██▒░▒████▓ "
ascii6 = blue+"▒ ▒▒ ▓▒░▓  ░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░░ ▒▓ ░▒▓░  ██▒▒▒  "+green+"  ░ ░▒ ▒  ░░ ▒░   ░  ░ ▒▒▓  ▒ "
ascii7 = blue+"░ ░▒ ▒░ ▒ ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░  ░▒ ░ ▒░▓██ ░▒░  "+green+"    ░  ▒   ░  ░      ░ ░ ▒  ▒ "
ascii8 = blue+"░ ░░ ░  ▒ ░ ░    ░    ░     ░░   ░   ░░   ░ ▒ ▒ ░░   "+green+"  ░        ░      ░    ░ ░  ░ "
ascii9 = blue+"░  ░    ░   ░         ░  ░   ░        ░     ░ ░      "+green+"  ░ ░             ░      ░    "
asciiA = blue+"                 ░                          ░ ░      "+green+"  ░                    ░      "

def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def command():
    print(ascii1+ascii2+ascii3+ascii4+ascii5+ascii6+ascii7+ascii8+ascii9+asciiA+"\n")

def receive_user_input():
    Fore.RESET
    userinp = input("anth@kiberry > ")
    system(userinp)
    
init()
clear()
command()

while True:
    receive_user_input()
