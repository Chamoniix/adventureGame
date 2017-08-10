# -*-coding:Latin-1 -*

from point import *
from mobDescriptor import *
import random

class Mob:

    def __init__(self, map):
        self.isdead = False
        #name, hpmax, attack, experienceReward, precision
        mobs = [MobDescriptor("Gobelin", 20, 10, 20, 80),
        MobDescriptor("rat", 10, 10, 10, 70),
        MobDescriptor("Troll", 100, 40, 100, 50),
        MobDescriptor("Sorcier", 30, 35, 50, 80)]
        i = random.randint(0,len(mobs)-1)
        self.name = mobs[i].name
        self.hp = mobs[i].hpMax
        self.hpMax = mobs[i].hpMax
        self.attack = mobs[i].attack
        self.experienceReward = mobs[i].experienceReward
        self.precision = mobs[i].precision
        self.dir = ["n", "s", "e", "w"]
        self.pos = Point(0,0)
        sX = len(map[:][1])
        sY = len(map[1][:])
        while 1:
            self.pos.x = random.randint(0,sX-1)
            self.pos.y = random.randint(0,sY-1)
            if map[self.pos.x][self.pos.y] == '.':
                break

    def move(self, map):
        dir = self.dir[random.randint(0,3)]
        if dir == "n" and self.pos.y < len(map.map[0][:])-1 :
            self.pos.y += 1
            return 0
        elif dir == "e" and self.pos.x < len(map.map[:][0])-1 :
            self.pos.x += 1
            return 0
        elif dir == "s" and self.pos.y > 0 :
            self.pos.y -= 1
            return 0
        elif dir == "w" and self.pos.x > 0 :
            self.pos.x -= 1
            return 0
        return -1

    def setPos(self, pos):
        self.pos = pos
