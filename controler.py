# -*-coding:Latin-1 -*

from joueur import *
import os

j = Joueur()
j.display()
res = 2
while 1 :
    clear()
    j.map.display()

    if (res < 0):
        print("Can't go this way")
    elif res == 2:
        print("start")
    else:
        print("You mooved")

    if not j.isOut():
        print("OUT")

    res = j.moove(input("Quelle direction ? "))
