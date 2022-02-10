from langs import langs
from interpreter import Interpreter as interpret
import os
os.system("cls")

a=langs['all']
o=''
for i in a:
    o+=i+' '

print("-"*(len(o)+1))
print(o)
print("-"*(len(o)+1))


def tryin():
    global lang
    lang = input("> ")
    if lang in a:
        os.system("cls")
        print("-"*(len(langs[lang]['main.welcome'])+1))
        print(langs[lang]['main.welcome'])
        print("-"*(len(langs[lang]['main.welcome'])+1))
        interpret(lang)
    else:
        tryin()

tryin()
