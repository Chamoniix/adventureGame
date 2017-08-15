# -*-coding:Latin-1 -*
import random
from point import *

class Usable:
    def __init__(self, map, lvl):
        usables = ['Potion', 'Big Potion','PREC+', 'HP+', 'ATK+']
        if -lvl < 5 :
            usables.append('Small Potion')
        self.name = usables[random.randint(0,len(usables)-1)]

        sX = len(map[:][1])
        sY = len(map[1][:])
        while 1:
            self.pos = Point(random.randint(0,sX-1),random.randint(0,sY-1))
            if map[self.pos.x][self.pos.y] == '.':
                break
