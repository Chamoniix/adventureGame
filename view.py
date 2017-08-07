# -*-coding:Latin-1 -*
import math
import os
clear = lambda: os.system('cls')

class View:

    def __init__(self):
        self.err = ""
        self.cmd = ['n', 's', 'e', 'w', 'd', 'i']


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
        return (nom, 1)

    def displayJoueur(self, j):
        clear()
        print ("################# ", j.name, " #################")
        print ("  + HP         : ", j.hp, "/", j.hpMax)
        print ("  + Attack     : ", j.attack)
        print ("  + Niveau     : ", j.niveau)
        print ("  + Experience : ", j.experience)

    def displayMap(self, j):
        for i in range (0,j.map.sizeY):
            l = "|"
            for k in range(0,j.map.sizeX):
                if (abs(j.x - k) + abs((j.map.sizeY-1 - j.y) - i)) < 3:
                    l=l+str(j.map.map[i][k])+" "
                else:
                    l=l+"  "
            l = l[0:len(l)-1] + "|"
            if (i == math.floor(j.map.sizeY/2)-1):
                l += "       Floor : " + str(j.map.lvl)
            if (i == math.floor(j.map.sizeY/2)):
                l += "       Difficulty : " + str(j.diff)
            print(l)

    def displayInfoCell(self, j):
        print (self.err)
        print ("> Vous etes en ", j.x, ",", j.y)
        if (j.isOut() == 0):
            print ("> Il y a un trou !")
        elif (j.map.map[j.x][j.y] == '.'):
            print ("> il n'y a rien sur cette case")


    def getInstruct(self):
        print("")
        while (1):
            act = input("Que voulez vous faire ?")
            if act in self.cmd:
                return act
            else:
                print("Unknown Command")


    def setErr(self, error):
        if error == -1:
            self.err = "YOU CAN'T GO THIS WAY"
        elif error == -2:
            self.err = "YOU CAN'T GO DOWN"
        elif error == 0:
            self.err = ""
