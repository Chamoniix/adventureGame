# -*-coding:Latin-1 -*

from map import *

class Joueur:
    def __init__(self):
        self.name = input("Entrez votre nom : ")
        self.x = 0
        self.y = 0
        self.map = Map()
        self.map.setCell(self.x, self.y,'x')
    def display(self):
        print("Joueur : ", self.name)
        print("  Position : ", self.x ,",", self.y)
        print("  map : ")
        self.map.display()

    def moove(self, dir):
        self.map.setCell(self.x,self.y,0)
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
            print ("n,s,e,w")
        res = self.map.setCell(self.x,self.y,'x')
        if res < 0:
            self.x = inix
            self.y = iniy
            self.map.setCell(self.x,self.y,'x')
            return -1
        else:
            return 0

# tests
if __name__ == "__main__":
    print ("TODO : TEST")
