# -*-coding:Latin-1 -*

from joueur import *
from view import *
import os

v = View()
clear()
res = v.menu()

if res == "1":
    nom, diff = v.createJoueur()
    j = Joueur(nom, diff)

quit = False
while (quit == False):
    v.displayJoueur(j)
    v.displayMap(j)
    v.displayInfoCell(j)
    instruct = v.getInstruct()
    err = j.act(instruct)
    v.setErr(err)




"""
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
"""
