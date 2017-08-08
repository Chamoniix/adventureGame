# -*-coding:Latin-1 -*

from map import *
import math

class Joueur:
    def __init__(self, nom, diff):
        self.name = nom
        self.hpMax = 100
        self.hp = 100
        self.attack = 10
        self.niveau = 1
        self.experience = 0
        self.upMsg = ""
        self.xpNeed = 10
        self.x = 0
        self.y = 0
        self.light = 3
        if diff == 1:
            self.diff = "Facile"
            self.mapSize = 4
        elif diff == 2:
            self.diff = "Moyen"
            self.mapSize = 7
        elif diff == 3:
            self.diff = "Dur"
            self.mapSize = 10
        self.map = Map(self.mapSize, self.mapSize)
        self.map.setCell(self.x, self.y,'x')
        self.objs = []

    def act(self, instruct):
        msg = ""
        if instruct == 'n' or instruct == 's' or instruct == 'e' or instruct == 'w':
            res = self.moove(instruct)
        elif instruct == 'd':
            res = self.down()
        elif instruct == 't':
            res, msg = self.take()
        return res, msg

    def down(self):
        if self.isOut() == 0:
            lvl = self.map.lvl
            self.experience += (-lvl+1) * 4
            self.testExp()
            del self.map
            self.map = Map(self.mapSize - lvl + 1 , self.mapSize - lvl + 1 , lvl-1)
            self.map.setCell(self.x, self.y,'x')
            return 0
        else:
            return -2

    def moove(self, dir):
        self.moveMobs()
        if (self.isOut() == 0):
            self.map.setCell(self.x,self.y,'o')
        elif (self.isOnObj() == 0):
            self.map.setCell(self.x,self.y,'#')
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

    def take(self):
        if self.isOnObj():
            return -3, ""
        else:
            self.map.obj.x = -1
            self.map.obj.y = -1
            nom = self.map.obj.nom
            self.objs.append(nom)
            if nom == "Torche":
                self.light +=1
            if nom == "Epe":
                self.attack +=10
            if nom == "Pierre":
                self.attack +=5
            if nom == "Armure":
                self.hp +=10

            self.experience += 10
            self.testExp()
            nom = "O" + nom
            return 0,nom

    def moveMobs(self):
        for i in range(0,len(self.map.mobs)):
            while 1 :
                x = self.map.mobs[i].pos.x
                y = self.map.mobs[i].pos.y

                res = self.map.mobs[i].move(self.map)
                if (not self.map.getCell(self.map.mobs[i].pos.x,self.map.mobs[i].pos.y) == '.') or (res == -1):
                    self.map.mobs[i].setPos(Point(x,y))
                else:
                    self.map.setCell(x, y, '.')
                    self.map.setCell(self.map.mobs[i].pos.x, self.map.mobs[i].pos.y, '@')
                    break


    def testExp(self):
        if self.experience > self.xpNeed :
            self.niveau += 1
            hp = random.randint(2,8)
            self.hp += hp
            self.hpMax += hp
            atk = random.randint(2,8)
            self.attack += atk
            if self.niveau == 5 :
                self.light += 1
            self.xpNeed = 2 * math.pow(2, self.niveau-1) * 10
            self.upMsg = "> LEVEL UP ! HP +" + str(hp) + ", ATK +" + str(atk)


    def isOut(self):
        if self.x == self.map.out.x and self.y == self.map.out.y:
            return 0
        else:
            return -1

    def isOnObj(self):
        if self.x == self.map.obj.x and self.y == self.map.obj.y:
            return 0
        else:
            return -1

# tests
if __name__ == "__main__":
    print ("TODO : TEST")
