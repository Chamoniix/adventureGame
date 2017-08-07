# -*-coding:Latin-1 -*

import os
clear = lambda: os.system('cls')

class View:
    def menu(self):
        clear()
        print ("Que voulez vous faire ?")
        print (" 1. Nouvelle Partie")
        print (" 2. Quitter")

        return input("")

    def createJoueur(self):
        clear()
        nom = input("Quel est le nom de votre joueur ? ")
        diff = input("Quel niveau de difficulte (Entre 1 et 3) ? ")
        return (nom, diff)

    def displayJoueur(self, j):
        clear()
        print ("################# ", j.name, " #################")
        print ("  + HP         : ", j.hp, "/", j.hpMax)
        print ("  + Attack     : ", j.attack)
        print ("  + Niveau     : ", j.niveau)
        print ("  + Experience : ", j.experience)
