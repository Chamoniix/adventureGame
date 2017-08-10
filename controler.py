# -*-coding:Latin-1 -*

from joueur import *
from view import *
from fight import *
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
    upmsg = ""
    """
    Display the next frame composed of :
        + Player status
        + The map
        + Info about the Cell
    """
    v.displayJoueur(j)
    v.displayMap(j)
    if not v.isAgro:
        v.displayInfoCell(j, msg)
    else:
        v.displayAgro()


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
        + 3 : Mob aggro
    """
    if not v.isAgro:
        res,msg,upmsg = j.act(instruct)
    else :
        coord = v.event.split(',')
        v.event = ""
        mob = None
        for i in range(len(j.map.mobs)):
            #print( "Mob n", i, " : " + j.map.mobs[i].name + "en position", j.map.mobs[i].pos.x,",",j.map.mobs[i].pos.y )
            if j.map.mobs[i].pos.x == int(coord[0]) and j.map.mobs[i].pos.y == int(coord[1]):
                mob = j.map.mobs[i]
        f = Fight(j, mob)
        res = f.fight()
        v.isAgro = False
        if res == 1 :
            v.displayJoueur(j)
            v.displayMap(j)
            v.displayInfoCell(j, msg)
            print(mob.name, " disparait...")
            input()
            j.map.setCell(mob.pos.x, mob.pos.y, '.')
            mob.setPos(Point(-1,-1))
            mob.isdead = True
            v.displayJoueur(j)
            v.displayMap(j)
            v.displayInfoCell(j, msg)
        if res == 2 :
            print("Joueur dead")
            input()
        if res == 3:
            print("Both KO")
            input()
        # TODO Delete mob


    """
    Sets Errors for next frame display
    """
    v.setErr(res, msg)


    """
    Sets Event for next frame display
    """
    v.setEvent(res, msg)

    """
    Set lvl up message
    """
    v.levelUp(upmsg)

    if res == 3 :
        v.setIsAgro(True, msg)
    else:
        v.setIsAgro(False)


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
