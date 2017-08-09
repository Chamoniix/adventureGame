

import os
import random
clear = lambda: os.system('cls')

class ViewFight:

    def __init__(self):
        self.x = 10
        self.attackStr1 = ""
        self.attackStr2 = ""
        self.msg = ""

    def displayHeader(self, j, mob):
        clear()
        stri = "#                         " + j.name + "  VS  " + mob.name
        while not len(stri) == 66:
            stri += " "
        stri += "#"
        print("###################################################################")
        print("#                                                                 #")
        print(stri)
        print("#                                                                 #")
        print("###################################################################")

        stri = "  + HP   : " + str(j.hp) + "/" + str(j.hpMax)
        while not len(stri) == 33:
            stri += " "
        stri += "|  + HP  :" + str(mob.hp) + "/" + str(mob.hpMax)
        print(stri)
        stri = "  + Attack   : " + str(j.attack)
        while not len(stri) == 33:
            stri += " "
        stri += "|  + Attack   : " + str(mob.attack)
        print(stri)
        print ("Usable    : ", j.usables)
        print ("XP reward : ", mob.experienceReward)

        print ()
        x =+ random.randint(-5,5)
        stri = "      " + - x * " " + "      (┛ò__ó)┛"+ x* " " +"   ╰(▲__▲)╯"
        print (stri)
        print ()
        print ()
        print (self.attackStr1)
        print (self.attackStr2)
        print ()
        print(self.msg)
        self.msg = ""
    def displayCmd(self):
        act = input ("Press Entre to attack, u to use objects  :  ")
        return act

    def displayHit(self, dmgJ, dmgM, jname, mname):
        self.attackStr1 = " > " + jname +   " inflige " + str(dmgJ) + " points de degats a " + mname + " !"
        self.attackStr2 = " > " + mname + " attaque, vous perdez " + str(dmgM) + " points de vie!"
