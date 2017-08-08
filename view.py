# -*-coding:Latin-1 -*
import math
import os
clear = lambda: os.system('cls')

class View:

    def __init__(self):
        self.err = ""
        self.obj = ""
        self.cmd = ['n', 's', 'e', 'w', 'd', 'i', 't', 'h']


    def menu(self):
        clear()
        print ("Que voulez vous faire ?")
        print (" 1. Nouvelle Partie")
        print (" 2. Quitter")

        return input("")

    def createJoueur(self):
        clear()
        nom = input("Quel est le nom de votre joueur ? ")

        while True :
            diff = input("Quel niveau de difficulte (Entre 1 et 3) ? ")
            diff = int(diff)
            if diff >=0 and diff <=3:
                break
        return (nom, diff)

    def displayJoueur(self, j):
        clear()
        print ("################# ", j.name, " #################")
        print ("  + HP         : ", j.hp, "/", j.hpMax)
        print ("  + Attack     : ", j.attack)
        print ("  + Niveau     : ", j.niveau)
        print ("  + Experience : ", j.experience, "/", j.xpNeed)
        print ("  + Inventaire : ", j.objs)

    def displayMap(self, j):
        for i in range (0,j.map.size.y):
            l = "|"
            for k in range(0,j.map.size.x):
                if (abs(j.x - k) + abs((j.map.size.y-1 - j.y) - i)) < j.light or 1 :
                    l=l+str(j.map.map[i][k])+" "
                else:
                    l=l+"  "
            l = l[0:len(l)-1] + "|"
            if (i == math.floor(j.map.size.y/2)-1):
                l += "       Floor : " + str(j.map.lvl)
            if (i == math.floor(j.map.size.y/2)):
                l += "       Difficulty : " + str(j.diff)
            print(l)

    def displayInfoCell(self, j, msg=""):
        print (self.err)
        print ("> Vous etes en ", j.x, ",", j.y)
        if msg == "LVLUP" :
            print("> LEVEL UP ! HP+, ATK+, DEF+")
        if (j.isOut() == 0):
            print ("> Il y a un trou !")
        elif (j.isOnObj() == 0):
            print ("> Il y a un Objet !")
        elif (not self.obj==""):
            print ( "> Vous avez recupere " + self.obj)
            self.obj = ""
        elif (j.map.map[j.x][j.y] == '.'):
            print ("> il n'y a rien sur cette case")

    def getInstruct(self):
        print("")
        while (1):
            act = input("Que voulez vous faire ?")
            if act in self.cmd:
                if act == 'h':
                    self.displayHelp()
                else:
                    return act
            else:
                print("Unknown Command")


    def setErr(self, error, msg = ""):
        if error == -1:
            self.err = "YOU CAN'T GO THIS WAY"
        elif error == -2:
            self.err = "YOU CAN'T GO DOWN"
        elif error == -3:
            self.err = "THERE IS NOTHING TO TAKE"
        elif error == 0 and not len(msg)==0:
            self.obj = msg[1:len(msg)]
        elif error == 0:
            self.err = ""

    def displayHelp(self):
        print("\nHELP : ")
        print("Commands :")
        print("    + n : North")
        print("    + s : South")
        print("    + e : East")
        print("    + w : West")
        print("    + d : Down")
        print("    + t : Take")
        print("    + h : Help")
        print("Map : ")
        print("    + . : Nothing")
        print("    + o : Hole")
        print("    + # : Object")
        print("    + @ : Ennemy")
        print("Objects : ")
        print("    + Torch  : +1 Light")
        print("    + Sword  : +10 attack")
        print("    + Rock   : +5 attack")
        print("    + Armor  : +10 hp")
