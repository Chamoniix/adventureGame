# -*-coding:Latin-1 -*

from map import *

class Joueur:
    def __init__(self, nom, diff):
        self.name = nom
        self.hpMax = 100
        self.hp = 100
        self.attack = 10
        self.niveau = 1
        self.experience = 0
        self.x = 0
        self.y = 0
        self.mapSize = 10
        self.map = Map(self.mapSize, self.mapSize)
        self.map.setCell(self.x, self.y,'x')
        if diff == 1:
            self.diff = "Facile"
        elif diff == 2:
            self.diff = "Moyen"
        elif diff == 3:
            self.diff = "Dur"

    def act(self, instruct):
        if instruct == 'n' or instruct == 's' or instruct == 'e' or instruct == 'w':
            res = self.moove(instruct)
        elif instruct == 'd':
            res = self.down()
        return res

    def down(self):
        if self.isOut() == 0:
            lvl = self.map.lvl
            del self.map
            if (lvl > -3):
                self.map = Map(10 , 10,lvl-1)
            elif lvl > -6:
                self.map = Map(15 , 15,lvl-1)
            else:
                self.map = Map(20, 20, lvl-1)
            self.map.setCell(self.x, self.y,'x')
            return 0
        else:
            return -2

    def moove(self, dir):
        if (self.isOut() == 0):
            self.map.setCell(self.x,self.y,'o')
        else:
            self.map.setCell(self.x,self.y,'.')
        inix = self.x
        iniy = self.y
        if dir == "n":
            self.y += 1
        elif dir == "e":
            self.x += 1
        elif dir == "s":
            self.y -= 1
        elif dir == "w":
            self.x -= 1
        else:
            return -1
        res = self.map.setCell(self.x,self.y,'x')
        if res < 0:
            self.x = inix
            self.y = iniy
            self.map.setCell(self.x,self.y,'x')
            return -1
        else:
            return 0

    def isOut(self):
        if self.x == self.map.outX and self.y == self.map.outY:
            return 0
        else:
            return -1

# tests
if __name__ == "__main__":
    print ("TODO : TEST")
