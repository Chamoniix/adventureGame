# -*-coding:Latin-1 -*

from object import *


class Map :
    """Class Map defined by :


    """
    def __init__(self, sX, sY, l=0):
        self.sizeX = sX
        self.sizeY = sY
        self.outX = random.randint(0,sX-1)
        self.outY = random.randint(0,sY-1)
        self.lvl = l
        self.map = [] #Cette liste contiendra ma map en 2D
        for i in range(self.sizeY):
            self.map.append(['.'] * self.sizeX)
        self.obj = Object(self.map)
        self.setCell(self.outX, self.outY, 'o')
        self.setCell(self.obj.x, self.obj.y, '#')


    def setCell(self, x, y, v):
        """ Permet de definir la valeur de la cellule [x][y]
        et de lui affecter la valeur v """
        if x >= 0 and x < self.sizeX and y >= 0 and y < self.sizeY:
            self.map[self.sizeY - 1 - y][x] = v
            return 0
        else:
            return -1



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
