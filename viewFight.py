# -*-coding:Latin-1 -*

import os
clear = lambda: os.system('cls')

class ViewFight:

    def __init__(self):
        self.attr = ""

    def displayHeader(self, jname, mobname):
        clear()
        print("############################################")
        print("#                                          #")
        print("#      " + jname + "  VS  " + mobname)
        print("#                                          #")
        print("############################################")
        input()
