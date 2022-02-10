import os
from langs import langs
from time import sleep as sl


def Interpreter(lang):
    cmdin = input("> ")
    if cmdin == f"{langs[lang]['main.cmds.exit']}":
        os.system("cls")
        for i in range(100):
            print("-"*(len(langs[lang]['main.exit_progress'])+1))
            print(langs[lang]['main.exit_progress'])
            print("-"*(len(langs[lang]['main.exit_progress'])+1))
            print(f"{i}%")
            sl(0)
            os.system("cls")
        os.system("cls")
        print("-"*(len(langs[lang]['main.exited'])+1))
        print(langs[lang]['main.exited'])
        print("-"*(len(langs[lang]['main.exited'])+1))
        sl(1)
        os.system("cls")