# -*-coding:Latin-1 -*
import random
import os
clear = lambda: os.system('cls')

class Object:

    def __init__(self, map):
        objects = ["Torche", "Fireball",
                "Epe en bois", "Epe en fer", "Epe du demon",
                "Anneau", "Amulette",
                 "Petite Armure", "Grosse Armure", "Bouclier",
                 "Masque"]
        sX = len(map[:][1])
        sY = len(map[1][:])
        self.nom = objects[random.randint(0,len(objects)-1)]
        while 1:
            self.x = random.randint(0,sX-1)
            self.y = random.randint(0,sY-1)
            if map[self.x][self.y] == '.':
                break
