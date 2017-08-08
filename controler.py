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
lvl = 0
while (quit == False):
    if not lvl == j.niveau:
        lvl = j.niveau
        msg = "LVLUP"
    v.displayJoueur(j)
    v.displayMap(j)
    v.displayInfoCell(j, msg)
    instruct = v.getInstruct()
    msg = ""
    err,msg = j.act(instruct)
    v.setErr(err, msg)




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
