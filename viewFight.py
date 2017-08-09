

import os
import random
clear = lambda: os.system('cls')

class ViewFight:

    def __init__(self):
        self.x = 10

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
        stri = "      " + -x* " " + "      (┛ò__ó)┛"+ x* " " +"   ╰(▲__▲)╯"
        print (stri)
        print ()




        input()
