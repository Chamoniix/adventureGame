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
        while 1:
            self.v.displayHeader(self.j, self.mob)
