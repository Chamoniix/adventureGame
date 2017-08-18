# -*-coding:Latin-1 -*

from joueur import *
from view import *
from fight import *
import os

class Controler:
    def __init__(self):
        self.v = View()
        clear()
        res = self.v.menu()

        if res == "1":
            nom, diff = self.v.createJoueur()
            self.j = Joueur(nom, diff)
        elif res == "2" :
            import pickle
            fileStr = "saves/" + input("What was your player name ?") + ".save"
            del self.v
            with open(fileStr, "rb") as f:
                self = pickle.load(f)
        elif res == "3" :
            exit()
        ''' Quit :
            + 1 : win
            + 2 : saved
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
            self.v.displayJoueur(self.j)
            self.v.displayMap(self.j)
            if not self.v.isAgro:
                self.v.displayInfoCell(self.j, msg)
            else:
                self.v.displayAgro()


            """
            Get Instruct Ask the next move to the user to verify that any mistakes has been done
            """
            instruct = self.v.getInstruct()


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
            if not self.v.isAgro:
                if instruct == 'u':
                    if (len(self.j.usables) == 0):
                        res = -4
                        msg = "Empty inventory"
                    else:
                        res = self.v.quelObjet(self.j.usables)
                        if not res == -1:
                            res, msg = self.j.use(res)
                            if res == 6:
                                quit = 1
                elif instruct == 'q':
                    if (input("Do you really want to save and quit ? (y/n)") == 'y'):
                        import pickle
                        strFile = "saves/" + self.j.name + ".save"
                        with open(strFile, "wb") as f:
                            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
                        quit = 2
                else:
                    res,msg,upmsg = self.j.act(instruct)
            else :
                if instruct == 'r':
                    if self.j.canRun :
                        input("You try to run away")
                        run = random.randint(0,100)
                        if run > 75:
                            print("You manage tu run")
                            input()
                            self.v.setIsAgro(False)
                            instruct = self.v.getInstruct()
                            res,msg,upmsg = self.j.act(instruct)

                            pass
                        else:
                            print("You are not fast enought")
                            input()
                            instruct = 'f'
                    else :
                        msg = "No shoes"
                        res = -6
                if instruct == 'f':
                    coord = self.v.event.split(',')
                    self.v.event = ""

                    mob = None
                    for i in range(len(self.j.map.mobs)):
                        #print( "Mob n", i, " : " + self.j.map.mobs[i].name + "en position", self.j.map.mobs[i].pos.x,",",self.j.map.mobs[i].pos.y )
                        if self.j.map.mobs[i].pos.x == int(coord[0]) and self.j.map.mobs[i].pos.y == int(coord[1]):
                            mob = self.j.map.mobs[i]
                    hp = self.j.hp
                    f = Fight(self.j, mob)
                    res = f.fight()
                    hp = hp - self.j.hp
                    self.v.setErr(0,"")
                    self.v.isAgro = False
                    if res == 1 :
                        self.v.displayJoueur(self.j)
                        self.v.displayMap(self.j)
                        self.v.displayInfoCell(self.j, msg)
                        print(mob.name, " disparait...")
                        print("Vous avez perdu ", hp, " points de vie.")
                        input()
                        self.j.map.setCell(mob.pos.x, mob.pos.y, '.')
                        self.j.experience += mob.experienceReward
                        mob.setPos(Point(-1,-1))
                        mob.isdead = True
                        self.v.displayJoueur(self.j)
                        self.v.displayMap(self.j)
                        self.v.displayInfoCell(self.j, msg)
                    if res == 2 :
                        quit = -1
                    if res == 3:
                        print("Both KO")
                        input()
                        quit = -1


            """
            Sets Errors for next frame display
            """
            self.v.setErr(res, msg)


            """
            Sets Event for next frame display
            """
            self.v.setEvent(res, msg)

            """
            Set lvl up message
            """
            self.v.levelUp(upmsg)

            if res == 3 :
                self.v.setIsAgro(True, msg)
            else:
                if not instruct == 'r':
                    self.v.setIsAgro(False)

        if quit == 1:
            self.v.win(self.j)
        elif quit == -1:
            c.lose(self.j)

if __name__ == "__main__":
    from controler import *
    controler = Controler()
