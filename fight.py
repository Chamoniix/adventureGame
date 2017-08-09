# -*-coding:Latin-1 -*

from joueur import *
from viewFight import *

class Fight:
    def __init__(self, j,mob):
        self.j = j
        self.mob = mob
        self.v = ViewFight()
        self.fight()

    def fight(self):
        self.v.displayHeader(self.j.name, self.mob.name)
