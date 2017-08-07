# -*-coding:Latin-1 -*
import math
import os
clear = lambda: os.system('cls')

class View:

    def __init__(self):
        self.err = ""


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
        print ("  + Experience : ", j.experience)

    def displayMap(self, j):
        for i in range (0,j.map.sizeY):
            l = "|"
            for k in range(0,j.map.sizeX):
                l=l+str(j.map.map[i][k])+" "
            l = l[0:len(l)-1] + "|"
            if (i == math.floor(j.map.sizeY/2)):
                l += "      Floor : " + str(j.map.lvl)
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
        return input("Que voulez vous faire ?")

    def setErr(self, error):
        if error == -1:
            self.err = "YOU CAN'T GO THIS WAY"
        elif error == 0:
            self.err = ""
