# -*-coding:Latin-1 -*
import math
import os
clear = lambda: os.system('cls')

class View:

    def __init__(self):
        self.err = ""
        self.isAgro = False
        self.event = ""
        self.upMsg = ""
        self.cmd = ['n', 's', 'e', 'w', 'd', 'i', 't', 'h']
        self.objDef = objects = {"Torche" : "la salle s'eclaire (LIGT +1)",
        "Fireball" : "Une explosion de lumiere ! (LIGT +3)",
        "Epe en bois" : "Petite epe en bois, plus efficace sur scene qu'en combat (ATK +5)",
        "Epe en fer" : "Une epe digne des plus grands forgerons (ATK +15)",
        "Epe du demon" : "La legende dit qu'elle est faite depuis la queue du demon... (ATK +50)",
        "Anneau" : "Un etrange anneau (???)",
        "Amulette" : "Une etrange amulette (???)",
        "Petite Armure" : "Une legere armure en cuire, elle vous sauvera des plus petits ennemis (HP +10)",
        "Grosse Armure" : "Une belle armure de chevalier (HP +25)",
        "Bouclier" : "Un authentique ecusson de chevalier (HP +20)"}


    def menu(self):
        clear()
        print ("Que voulez vous faire ?")
        print (" 1. Nouvelle Partie")
        print (" 2. Quitter")

        return input("")

    def createJoueur(self):
        clear()
        nom = input("Quel est le nom de votre joueur ? ")

        while True :
            diff = input("Quel niveau de difficulte (Entre 1 et 3) ? ")
            diff = int(diff)
            if diff >=0 and diff <=3:
                break
        return (nom, diff)

    def displayJoueur(self, j):
        clear()
        print ("################# ", j.name, " #################")
        print ("  + HP         : ", j.hp, "/", j.hpMax)
        print ("  + Attack     : ", j.attack)
        print ("  + Niveau     : ", j.niveau)
        print ("  + Experience : ", j.experience, "/", j.xpNeed)
        print ("  + Inventaire : ", j.objs)

    def displayMap(self, j):
        for i in range (0,j.map.size.y):
            l = "|"
            for k in range(0,j.map.size.x):
                if (abs(j.x - k) + abs((j.map.size.y-1 - j.y) - i)) < j.light  or 1 :
                    l=l+str(j.map.map[i][k])+" "
                else:
                    l=l+"  "
            l = l[0:len(l)-1] + "|"
            if (i == math.floor(j.map.size.y/2)-1):
                l += "       Floor : " + str(j.map.lvl)
            if (i == math.floor(j.map.size.y/2)):
                l += "       Difficulty : " + str(j.diff)
            print(l)

    def displayInfoCell(self, j, msg=""):
        print()
        ''' Zone affichant l'erreur s'il y en a eu une '''
        print ("# ", self.err)

        ''' Coordonnees et ce qui se trouve sur la cellule '''
        print ("+ Vous etes en ", j.x, ",", j.y)
        if (j.isOut() == 0):
            print ("+ Il y a un trou !")
        elif (j.isOnObj() == 0):
            print ("+ Il y a un Objet !")
        elif (j.map.map[j.x][j.y] == '.'):
            print ("+ il n'y a rien sur cette case")

        ''' Affiche les evenements precedents '''
        print ("> ", self.event)

        ''' Affiche un message si le joueur a gagné un niveau '''
        if not self.upMsg == "":
            print ("> ", self.upMsg)

    def displayAgro(self):
        print()
        print("############################################")
        print("#                                          #")
        print("#      Un monstre vous agresse !           #")
        print("#                                          #")
        print("############################################")

    def getInstruct(self):
        print("")
        while (1):
            act = input("Que voulez vous faire ?")
            act = act[0]
            if not self.isAgro:
                if act in self.cmd:
                    if act == 'h':
                        self.displayHelp()
                    else:
                        return act
                else:
                    print("Unknown Command, 'h' for help")
            else:
                if act in ['h', 'f', 'r']:
                    if act == 'h':
                        self.displayHelp()
                    else:
                        return act
                else:
                    if act in self.cmd:
                        print("This is no time for this...")
                    else:
                        print("Unknown Command, 'h' for help")


    def setErr(self, error, msg = ""):
        if error == -1:
            self.err = "YOU CAN'T GO THIS WAY"
        elif error == -2:
            self.err = "YOU CAN'T GO DOWN"
        elif error == -3:
            self.err = "THERE IS NOTHING TO TAKE"
        elif error == 0:
            self.err = ""

    def setEvent(self, event, msg = ""):
        if event == 1 and msg[0:3] == "OBJ":
            self.event =  "Vous avez recupere " + msg[3:len(msg)] + "\n>>> " + self.objDef[msg[3:len(msg)]]
        elif event == 2:
            self.event = "Vous tombez dans une nouvelle piece"
        elif event == 0:
            self.event = ""

    def levelUp(self, msg):
        self.upMsg = msg

    def setIsAgro(self, yn):
        self.isAgro = yn

    def displayHelp(self):
        print("\nHELP : ")
        print("Commands :")
        print("    + n : North")
        print("    + s : South")
        print("    + e : East")
        print("    + w : West")
        print("    + d : Down")
        print("    + t : Take")
        print("    + h : Help")
        print("Map : ")
        print("    + . : Nothing")
        print("    + o : Hole")
        print("    + # : Object")
        print("    + @ : Ennemy")
        print("Objects : ")
        print("    + Torch  : +1 Light")
        print("    + Sword  : +10 attack")
        print("    + Rock   : +5 attack")
        print("    + Armor  : +10 hp")
