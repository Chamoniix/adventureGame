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

''' Quit :
    + 1 : win
    - 1 : lose
    '''
quit = 0
while (quit == 0):
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
        - 4 : Empty inventory
        - 5 : Full HP can't use
        - 6 : No Shoes, can't run
        + 1 : Found an object, display efects
        + 2 : New floor
        + 3 : Mob aggro
        + 4 : Found an usable, display name
        + 5 : Object used, display effect
        + 6 : Use last object
    """
    if not v.isAgro:
        if instruct == 'u':
            if (len(j.usables) == 0):
                res = -4
                msg = "Empty inventory"
            else:
                res = v.quelObjet(j.usables)
                if not res == -1:
                    res, msg = j.use(res)
                    if res == 6:
                        quit = 1
        else:
            res,msg,upmsg = j.act(instruct)
    else :
        if instruct == 'r':
            if j.canRun :
                input("You try to run away")
                run = random.randint(0,100)
                if run > 75:
                    print("You manage tu run")
                    input()
                    v.setIsAgro(False)
                    instruct = v.getInstruct()
                    res,msg,upmsg = j.act(instruct)

                    pass
                else:
                    print("You are not fast enought")
                    input()
                    instruct = 'f'
            else :
                msg = "No shoes"
                res = -6
        if instruct == 'f':
            coord = v.event.split(',')
            v.event = ""

            mob = None
            for i in range(len(j.map.mobs)):
                #print( "Mob n", i, " : " + j.map.mobs[i].name + "en position", j.map.mobs[i].pos.x,",",j.map.mobs[i].pos.y )
                if j.map.mobs[i].pos.x == int(coord[0]) and j.map.mobs[i].pos.y == int(coord[1]):
                    mob = j.map.mobs[i]
            hp = j.hp
            f = Fight(j, mob)
            res = f.fight()
            hp = hp - j.hp
            v.setErr(0,"")
            v.isAgro = False
            if res == 1 :
                v.displayJoueur(j)
                v.displayMap(j)
                v.displayInfoCell(j, msg)
                print(mob.name, " disparait...")
                print("Vous avez perdu ", hp, " points de vie.")
                input()
                j.map.setCell(mob.pos.x, mob.pos.y, '.')
                j.experience += mob.experienceReward
                mob.setPos(Point(-1,-1))
                mob.isdead = True
                v.displayJoueur(j)
                v.displayMap(j)
                v.displayInfoCell(j, msg)
            if res == 2 :
                quit = -1
            if res == 3:
                print("Both KO")
                input()
                quit = -1


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
        if not instruct == 'r':
            v.setIsAgro(False)

if quit == 1:
    v.win(j)
elif quit == -1:
    c.lose(j)

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
