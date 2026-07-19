import time
import subprocess as sub
import cowthepro as co
import terminalthepro as term
import cat_os as cs
import hexcmd
import pyttsx3 as py
import random as ran
from cat_os import meow, nerd, play, playA, playB, story
import sys
import os
from terminalthepro import modeL, modeNL, test
sys.stderr = open(os.devnull, 'w')

def su():
    ss = input("sh: ")
    sub.run(f"{ss}", shell=True)
def suL():
    sst = input("sh: ")
    print("Loading...")
    time.sleep(3)
    sub.run(f"{sst}", shell=True)
def diceroll(T=None, Pick=None, DD=None):
    if T is None and Pick is None and DD is None:
        print(ran.randint(1,6))
    elif T is not None:
        print(ran.randint(1,1000000000000))
    elif Pick is not None:
        dtp = input("pick (use ,): ")
        low, high = map(int, dtp.split(","))
        print(ran.randint(low, high))
    elif DD is not None:
        a = ran.randint(1,6)
        b = ran.randint(1,6)
        print("dice one:", a)
        print("dice two:", b)
        print("total:", a + b)
def pyttsx3(test=None, say=None):
    en = py.init()
    if test is not None:
        en.say("Code 0")
        en.runAndWait()
    if say is not None:
        pts = input("say: ")
        en.say(f"{pts}")
        en.runAndWait()
def cat(name=None, test=None, boot=None):
    if name is not None:
        print("Hi my name is luna")
    elif test is not None:
        print("Code 0")
    elif boot is not None:
        print("meow, nerd, play, playA, playB, story")
        p = input("Pick: ")
        if p in ["meow", "nerd", "play", "playA", "playB", "story"]:
            if p in ["meow", "Meow"]:
                meow()
            elif p in ["nerd",  "Nerd"]:
                nerd()
            elif p in ["play", "Play"]:
                play("vid")
            elif p in ["playA", "PlayA"]:
                playA("cat")
            elif p in ["playB", "PlayB"]:
                playB("BFF")
            elif p in ["story", "Story"]:
                story("luna")
def catpick(meow_v=None, nerd_v=None, play_v=None, playA_v=None, playB_v=None, story_v=None):
    if meow_v is not None:
        meow()
    elif nerd_v is not None:
        nerd()
    elif play_v is not None:
        play("vid")
    elif playA_v is not None:
        playA("cat")
    elif playB_v is not None:
        playB("BFF")
    elif story_v is not None:
        story("luna")
def term(test_v=None, modeNL_v=None, modeL_v=None):
    if test_v is not None:
        test()
    elif modeNL_v is not None:
        modeNL()
    elif modeL_v is not None:
        modeL()
def cal(test_v=None, cowp_v=None, cowm_v=None, cowt_v=None, cowd_v=None):
    if test_v is not None:
        co.test()
    if cowp_v is not None:
        co.cowp()
    if  cowm_v is not None:
        co.cowm()
    if cowt_v is not None:
        co.cowt()
    if cowd_v is not None:
        co.cowd()
def python(test=None, python_v=None):
    if test is not None:
        print("Code 0")
    elif python is not None:
        pythn = input("python: ")
        exec(pythn)
def made():
    print("Made By: Leo\nHelp By: Stuart\nMade on: 2026-07-16 06:40:42")