# -*-coding:Latin-1 -*

from object import *
from mob import *
from usable import *

class Map :
    """Class Map defined by :


    """
    def __init__(self, sX, sY, l=0):
        self.shadow = True
        self.size = Point(sX, sY)
        self.out = Point(random.randint(0,sX-1), random.randint(0,sY-1))
        self.lvl = l
        self.map = [] #Cette liste contiendra ma map en 2D
        for i in range(self.size.y):
            self.map.append(['.'] * self.size.x)
        self.obj = Object(self.map)
        self.usbl = Usable(self.map, self.lvl)
        self.mobs = []
        self.setCell(self.out.x, self.out.y, 'o')
        self.setCell(self.obj.x, self.obj.y, '#')
        self.setCell(self.usbl.pos.x, self.usbl.pos.y, '~')

        if l == 0 :
            pass
        elif l == -1:
            self.addMob(2)
        elif l == -2:
            self.addMob(4)
        elif l == -3:
            self.addMob(5)
        elif l == -4:
            self.addMob(6)
        elif l == -5:
            self.addMob(7)
        elif l == -6:
            self.addMob(8)
        elif l == -7:
            self.addMob(8)
        elif l == -8:
            self.addMob(9)
        elif l == -9:
            self.addMob(13)
        elif -l == 10:
            self.shadow = False
            self.setCell(self.out.x, self.out.y, '.')
            self.out.x = -1
            self.out.y = -1
            self.setCell(self.usbl.pos.x, self.usbl.pos.y, '.')
            self.usbl = Usable(self.map,self.lvl, "Un oeuf")
            self.setCell(self.usbl.pos.x, self.usbl.pos.y, '~')

    def addMob(self, nb):
        for i in range(0,nb):
            mob = Mob(self.map, self.lvl)
            self.setCell(mob.pos.x, mob.pos.y, '@')
            self.mobs.append(mob)

    def setCell(self, x, y, v):
        """ Permet de definir la valeur de la cellule [x][y]
        et de lui affecter la valeur v """
        if x >= 0 and x < self.size.x and y >= 0 and y < self.size.y:
            self.map[self.size.y - 1 - y][x] = v
            return 0
        else:
            return -1
    def getCell(self, x, y):
        return self.map[self.size.y - 1 - y][x]


# tests
if __name__ == "__main__":
        m = Map(20,20)
        if not m.setCell(10, 10, 3):
            print (">OK")
        else:
            print("Err")
        if not m.setCell(5, 5, 1):
            print (">OK")
        else:
            print("Err")
        if (m.setCell(30, 25, 3)):
            print (">OK")
        else:
            print("Err")
        m.display()
