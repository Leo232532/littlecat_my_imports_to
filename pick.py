import littlecat
from littlecat import diceroll, su, suL, cat, pyttsx3, cal, python, made
import time

def mainpart():
    print("Welcome to littlecat import (by Leo)!")
    print("What do you want to do?")
    print("-------------------------------------")
    print("1. Roll a dice")
    print("2. Do some Shell")
    print("3. Play with luna!")
    print("4. Make the COM talk")
    print("5. Do some math with the calculator")
    print("6. Like 2 but it Python")
    print("7. Made by")
    print("8. quit")
    c = input("A: ")
    return c
def redoQ():
    print("Do again?")
    print("---------")
    print("1. yes")
    print("2. no")
    ccc = input("A: ")
    if ccc == "1":
        diceroll(T="yes")
    elif ccc == "2":
        exit()
while True:
    c = mainpart()
    if c in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        if c == "1":
            print("Roll a dice")
            print("-----------")
            print("1. 1-1000000000000")
            print("2. 1-6")
            print("3. Double dice")
            print("4. Back")
            cc = input("A: ")
            if cc in ["1", "2", "3", "4"]:
                if cc == "1":
                    diceroll(T="yes")
                    time.sleep(2)
                    redoQ()
                elif cc == "2":
                    diceroll()
                    time.sleep(2)
                    redoQ()
                elif cc == "3":
                    diceroll(DD="yes")
                    time.sleep(2)
                    redoQ()
                elif cc == "4":
                    continue
        elif c == "2":
            while True:
                print("Do some shell")
                print("-------------")
                print("1. Loading")
                print("2. Nonloading")
                print("3. Back")
                cccc = input("A: ")
                if cccc == "1":
                    suL()
                    time.sleep(6.5)
                    break
                elif cccc == "2":
                    su()
                    time.sleep(6.5)
                    break
                elif cccc == "3":
                    break
        elif c == "3":
            while True:
                print("Play with luna")
                print("--------------")
                print("1. Start")
                print("2. Back")
                c5 = input("A: ")
                if c5 == "1":
                    print("Starting...")
                    time.sleep(4)
                    cat(boot="yes")
                    break
                elif c5 == "2":
                    break
        elif c == "4":
            while True:
                print("Make the COM talk")
                print("-----------------")
                print("1. Start")
                print("2. Back")
                c6 = input("A: ")
                if c6 == "1":
                    print("Starting...")
                    time.sleep(3)
                    pyttsx3(say="yes")
                    break
                elif c6 == "2":
                    break
        elif c == "5":
            while True:
                print("Do some math with the calculator")
                print("--------------------------------")
                print("1. +")
                print("2. -")
                print("3. x")
                print("4. /")
                print("5. Back")
                c7 = input("A: ")
                if c7 == "1":
                    cal(cowp_v="yes")
                    time.sleep(4)
                    break
                elif c7 == "2":
                    cal(cowm_v="yes")
                    time.sleep(4)
                    break
                elif c7 == "3":
                    cal(cowt_v="yes")
                    time.sleep(4)
                    break
                elif c7 == "4":
                    cal(cowd_v="yes")
                    time.sleep(4)
                    break
                elif c7 == "5":
                    break
        elif c == "6":
            while True:
                print("Like 2 but it Python")
                print("--------------------")
                print("1. Start")
                print("2. Back")
                c8 = input("A: ")
                if c8 == "1":
                    python(python_v="yes")
                    time.sleep(4)
                    break
                elif c8 == "1":
                    break
        elif c == "7":
            made()
        elif c == "8":
            exit()
    else:
        while True:
            print("Help")
            print("----")
            print("Pls type a available number")
            time.sleep(3)
            break