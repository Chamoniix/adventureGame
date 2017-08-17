# -*-coding:Latin-1 -*

from joueur import *
from viewFight import *
import math

class Fight:
    def __init__(self, j,mob):
        self.j = j
        self.mob = mob
        self.v = ViewFight()
        if mob.name == "Spectre":
            self.savedPrec = j.precision
            j.precision = 15
    ''' returns :
        + 1 : Mob died
        + 2 : Joueur died
        + 3 : Both Died
        '''

    def fight(self):

        while 1:
            self.v.displayHeader(self.j, self.mob)
            act = self.v.displayCmd()

            if act == "":
                dmgJ, dmgM = self.attack()
                res = self.isDead()
                if not res == 0:
                    self.v.displayHit(dmgJ, dmgM, self.j.name, self.mob.name)
                    self.v.displayHeader(self.j, self.mob)
                    if res == 1:
                        print (self.mob.name, " is dead.")
                    elif res == 2:
                        print (self.j.name, " is dead.")
                    elif res == 3:
                        print (self.mob.name, " and ", self.j.name, " are dead.")
                    input()
                    if self.mob.name == "Spectre":
                        self.j.precision = self.savedPrec
                    return res
                self.v.displayHit(dmgJ, dmgM, self.j.name, self.mob.name)

            elif act == "u":
                self.v.msg = "USE : " + str(self.j.usables)
            else:
                v.msg = "Unknown command"



    def attack(self):
        dmgJ = math.floor((self.j.attack - random.randint(0,math.floor(self.j.attack/2)))/2)
        dmgM = math.floor((self.mob.attack - random.randint(0,math.floor(self.mob.attack/2)))/2)

        touche = random.randint(0,100)
        if touche > self.j.precision:
            dmgJ = 0
        touche = random.randint(0,100)
        if touche > self.mob.precision:
            dmgM = 0

        self.j.hp -= dmgM
        self.mob.hp -= dmgJ

        return dmgJ, dmgM

    ''' returns :
        + 0 : No one died
        + 1 : Mob died
        + 2 : Joueur died
        + 3 : Both Died
        '''
    def isDead(self):
        res = 0
        if self.mob.hp <= 0:
            self.mob.hp = 0
            res += 1
        if self.j.hp <= 0:
            self.j.hp = 0
            res += 2
        return res

# tests
if __name__ == "__main__":
    j = Joueur("Hugo", 3)
    mob = Mob(j.map.map)
    fght = Fight(j, mob)
