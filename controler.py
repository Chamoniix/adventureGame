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
    msg = ""

    """
    Display the next frame composed of :
        + Player status
        + The map
        + Info about the Cell
    """
    v.displayJoueur(j)
    v.displayMap(j)
    v.displayInfoCell(j, msg)


    """
    Get Instruct Ask the next move to the user to verify that any mistakes has been done
    """
    instruct = v.getInstruct()


    """
    Every actions on the model are done by act function from Joueur.
    It return :
        + A code statu with can identify what happened
        + A message which can be usefull for display e.g. object name

    Status are made this way : Negative => Error, Positiv => Evemt :
          0 : No display
        - 1 : Impossible direction
        - 2 : Not on the exit, can't use down
        - 3 : Not on an object, can't use take
        + 1 : Found an object, display efects
        + 2 : New floor
    """
    res,msg = j.act(instruct)
    testLvlUp(j)

    """
    Sets Errors for next frame display
    """
    v.setErr(res, msg)


    """
    Sets Event for next frame display
    """
    v.setEvent(res, msg)



    def testLvlUp(self, j):
        if 

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
