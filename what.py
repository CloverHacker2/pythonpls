import time

import random

import sys

import colorama

from colorama import Fore, Back, Style

pss = ["ohyeah"]
def error():
    print(Fore.RED + "ERROR, CODE NOT DEFINED")
    time.sleep(2)
    print(Fore.LIGHTYELLOW_EX + "RESTARTING...")
    print(Fore.RESET)
    time.sleep(2)

def IES():
    print (Fore.LIGHTYELLOW_EX + "RESTARTING IMMEDIATLY...")

def ps(str):
    sys.stdout.write("\n")
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.03)

def entry(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.4)

entry("WHAT IS YOUR NAME???\n")
name = input()
ps(Fore.RED + "ATTENTION. THIS COMPUTER IS NOT CONNECTED TO SECURE NETWORK.")
time.sleep(2)
ps(Fore.RED + "SECURING MOMENTARILY...")
time.sleep(4)
ps(Fore.LIGHTYELLOW_EX + "WE REQUIRE A PASSCODE. WHAT IS THE UNIVERSAL PASSCODE? " + Fore.GREEN + "Hey, it's IGEA.\n")
x = input(Fore.RESET)
if (x == "IGEA"):
    while(True):
        ps(Fore.RESET + "Welcome, " + name + "! Thank you for securing the IGEA terminal, version 225.7.")
        time.sleep(2)
        ps("Please enter a command among the following: login, access, logout.\n")
        x = input()
        if (x in pss):
            ps(Fore.GREEN + "ACCESS GRANTED. WELCOME, " + name.upper() + ".")
            time.sleep(2)
            ps("PLEASE WAIT AS WE ACCESS THE LATEST STATUS REPORT...")
            time.sleep(2)
            ps(Fore.RED + "ATTENTION OFFICE OF THE DIRECTOR. \n\nTHIS STATUS REPORT IS TO UPDATE THE IGEA OFFICIALLY ON THE CURRENT WORRIES OF THE SHIP FROM DIM. \n\nTHE SHIP HAS BEEN DESTROYED, AND REQUIRES A REPLACEMENT. \n\nALL IM AGENTS ARE SAFE.")
            time.sleep(2)
            ps(Fore.RESET + "Would you like to reset? y/n\n")
            x = input()
            while(x not in ["y","n"]):
                ps(Fore.RESET + "Would you like to reset? y/n\n")
                x = input()
                if (x not in ["y","n"]):
                    ps(Fore.RED + "Nope, try something else.")
                elif (x == "y"):
                    IES()
                elif (x == "n"):
                    exit()
        elif (x == "exit"):
            break
        else:
            error()

