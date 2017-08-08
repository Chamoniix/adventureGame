# -*-coding:Latin-1 -*
import random
import os
clear = lambda: os.system('cls')

class Object:

    def __init__(self, map):
        objects = ["Torche", "Epe", "Anneau", "Amulette", "Armure", "Pierre", "Potion", "Food"]
        sX = len(map[:][1])
        sY = len(map[1][:])
        self.nom = objects[random.randint(0,len(objects)-1)]
        while 1:
            self.x = random.randint(0,sX-1)
            self.y = random.randint(0,sY-1)
            if map[self.x][self.y] == '.':
                break
