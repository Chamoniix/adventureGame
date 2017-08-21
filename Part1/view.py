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
        self.cmd = ['n', 's', 'e', 'w', 'd', 'i', 't', 'h', 'u', 'q']
        self.objDef = {"Torche" : "la salle s'eclaire (LIGT +1)",
        "Fireball" : "Une explosion de lumiere ! (LIGT +3)",
        "Epe en bois" : "Petite epe en bois, plus efficace sur scene qu'en combat (ATK +5)",
        "Epe en fer" : "Une epe digne des plus grands forgerons (ATK +15)",
        "Epe du demon" : "La legende dit qu'elle est faite depuis la queue du demon... (ATK +50)",
        "Anneau" : "Un etrange anneau (???)",
        "Amulette" : "L'amullette vous permet de voir les ombres dans l'obscurite...",
        "Petite Armure" : "Une legere armure en cuire, elle vous sauvera des plus petits ennemis (HP +10)",
        "Grosse Armure" : "Une belle armure de chevalier (HP +25)",
        "Bouclier" : "Un authentique ecusson de chevalier (HP +20)",
        "Masque" : "Vous faites peur aux ennemis, ils vous attaquent de plus loin (AGRO +1)",
        "Shoes": "Vous pouvez maintenant essayer de vous enfuire lorsqu'un monstre vous attaque !"}
        self.usblDef = {'Small Potion' : "HP +10",
        'Potion' : "HP + 100",
        'Big Potion': "HP max !",
        'HP+' : "HP+20",
        'ATK+': "ATK+10",
        'PREC+': "PREC+5",
        'Un oeuf' : "Vous trouvez un oeuf etrange... vous le mettez au chaud dans votre sac"}

    def menu(self):
        res = ['1', '2']
        while 1:
            clear()
            print ("Que voulez vous faire ?")
            print (" 1. Nouvelle Partie")
            print (" 2. Charger")
            print (" 3. Quitter")
            r = input("")
            if r in res:
                break
        return r

    def createJoueur(self):
        clear()
        nom = input("Quel est le nom de votre joueur ? ")
        res = ['1', '2', '3']
        while True :
            diff = input("Quel niveau de difficulte (Entre 1 et 3) ? ")
            if diff in res:
                diff = int(diff)
                return nom,diff


    def displayJoueur(self, j):
        exp = math.floor(20 * j.experience / j.xpNeed)
        strExp = '|'
        for i in range(0,exp):
            strExp += '#'
        while len(strExp) < 21:
            strExp += ' '
        strExp += '|'
        clear()
        print ("################# ", j.name, " #################")
        print ("  + HP         : ", j.hp, "/", j.hpMax)
        print ("  + Attack     : ", j.attack)
        print ("  + precision : ", j.precision)
        print ("  + Niveau     : ", j.niveau)
        print ("  + Experience : ", strExp)
        print ("  + Equipement : ", j.objs)

    def displayMap(self, j):
        for i in range (0,j.map.size.y):
            l = "|"
            for k in range(0,j.map.size.x):
                if (abs(j.x - k) + abs((j.map.size.y-1 - j.y) - i)) < j.light or j.map.shadow == False:
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
        elif (j.isOnUsable() == 0):
            print ("+ Il y a quelque chose sur le sol...")
        elif (j.map.map[j.x][j.y] == '.'):
            print ("+ il n'y a rien sur cette case")

        ''' Affiche les evenements precedents '''
        print ("> ", self.event)

        ''' Affiche un message si le joueur a gagné un niveau '''
        if not self.upMsg == "":
            print ("> ", self.upMsg)

    def displayAgro(self):
        print(self.err)
        print("############################################")
        print("#                                          #")
        print("#      Un monstre vous agresse !           #")
        print("#                                          #")
        print("############################################")

    def quelObjet(self, objs):
        clear()
        print("############################################")
        print("#                                          #")
        print("#                INVENTAIRE                #")
        print("#                                          #")
        print("############################################")
        print("       ________     ________   ")
        print("       |      |     |      |   ")
        print("   /'''''''''''''''''''''''''\ ")
        print("  /                           \ ")
        print("  |                            |")
        print("  (     | |          | |       )")
        print("  |     |'|          |'|       |")
        print("  (                            )")
        print("  |    ###                     |")
        print("  |    ###   ###      Addidas  |")
        print("  |    ###   ###   ###         |")
        print("  \    ###   ###   ###        / ")
        print("   \_________________________/")
        print()
        print()
        print("You have : ")
        results = []
        for i in range(0,len(objs)):
            print("    ", i+1, ". ", objs[i])
            results.append(str(i+1))
        print("    ", "c", ". Press c to cancel")

        print()
        while 1 :
            res = input("Que voulez vous utiliser ?")
            if res == 'c':
                return -1
            elif res in results :
                break
            else :
                print("Entrez le numero correspondant a l'objet que vous voulez utiliser")
        return res



    def getInstruct(self):
        print("")
        while (1):
            act = input("Que voulez vous faire ?")
            if len(act) >0:
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
        elif error == -4:
            self.err = "THERE IS NOTHING IN YOUR INVENTORY"
        elif error == -5:
            self.err = "FULL HP, YOU CAN'T USE THIS"
        elif error == -6:
            self.err = "YOU HAVE NO SHOES, YOU CAN'T RUN"
        elif error == 0:
            self.err = ""

    def setEvent(self, event, msg = ""):
        if event == 1 and msg[0:3] == "OBJ":
            self.event =  "Vous avez recupere " + msg[3:len(msg)] + "\n>>> " + self.objDef[msg[3:len(msg)]]
        elif event == 2:
            self.event = "Vous tombez dans une nouvelle piece"
        if event == 4 and msg[0:4] == "USBL":
            self.event =  "Vous avez trouve un objet utilisable : " + msg[4:len(msg)] + " !\n>>> Utilisez 'u' pour ouvrir l'inventaire"
        if event == 5:
            self.event =  "Vous avez utilise " + msg + ".\n>>> " + self.usblDef[msg]
        elif event == 0:
            self.event = ""

    def levelUp(self, msg):
        self.upMsg = msg

    def setIsAgro(self, yn,msg=""):
        self.isAgro = yn
        if yn:
            self.event = msg


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
        print("    + u : use")
        print("    + f : fight")
        print("    + r : run")
        print("Map : ")
        print("    + . : Nothing")
        print("    + o : Hole")
        print("    + # : Object")
        print("    + @ : Ennemy")
        print("Objects : ")
        print("    + Torche        : la salle s'eclaire (LIGT +1)")
        print("    + Fireball      : Une explosion de lumiere ! (LIGT +3)")
        print("    + Epe en bois   : Petite epe en bois, plus efficace sur scene qu'en combat (ATK +5)")
        print("    + Epe en fer    : Une epe digne des plus grands forgerons (ATK +15)")
        print("    + Epe du demon  : La legende dit qu'elle est faite depuis la queue du demon... (ATK +50)")
        print("    + Anneau        : Un etrange anneau (???)")
        print("    + Amulette      : Une etrange amulette (???)")
        print("    + Petite Armure : Une legere armure en cuire, elle vous sauvera des plus petits ennemis (HP +10)")
        print("    + Grosse Armure : Une belle armure de chevalier (HP +25)")
        print("    + Bouclier      : Un authentique ecusson de chevalier (HP +20)")
        print("    + Masque        : Vous faites peur aux ennemis, ils vous attaquent de plus loin (AGRO +1)")




    def win(self, j):
        import random
        import time
        import webbrowser
        import inspect
        import json
        def buildLine(txt):
            if len(txt) < 30:
                chars = ['~','#','@']
                line = ""
                nbSpaces = math.floor((50 - len(txt))/2)
                for i in range(0,20):
                    line += chars[random.randint(0,len(chars)-1)]
                for i in range(0, nbSpaces):
                    line += ' '
                line+= txt
                while  len(line) < 70:
                    line += ' '
                for i in range(0,20):
                    line += chars[random.randint(0,len(chars)-1)]
                return line
            else :
                return "Trop long"


        line = []
        line.append(buildLine(" "))
        line.append(buildLine(" "))
        line.append(buildLine("Good Game"))
        line.append(buildLine(" "))
        line.append(buildLine(" "))
        line.append(buildLine(" "))
        line.append(buildLine("Stats finales : "))
        line.append(buildLine("lvl " + str(j.niveau)))
        line.append(buildLine("Attaque " + str(j.attack)))
        line.append(buildLine("HP " + str(j.hpMax)))
        line.append(buildLine("Precision " + str(j.precision)))
        line.append(buildLine(" "))
        line.append(buildLine(" "))
        line.append(buildLine(" "))
        line.append(buildLine("SCORE : 8973548"))
        line.append(buildLine(" "))
        line.append(buildLine("Bravo."))
        for i in range(0, len(line)):
            clear()
            for k in range(0, len(line)-1):
                if k>=i:
                    print(line[k])
                else:
                    print()
            if i == 0:
                input()
            else:
                time.sleep(0.2)
        clear()
        time.sleep(1)
        for k in range(0, len(line)-1):
            if k == 8:
                print("               Un gaz bizarre s'echappe de l'oeuf...          ")
            else:
                print()
        playerStat = {'hpMax' : j.hpMax,
        'hp' : j.hp,
        'attack'  : j.attack,
        'precesion' : j.precision,
        'lvl' : j.niveau,
        'Objects' : j.objs,
        'Usables' : j.usables}
        with open('.tmp', 'w') as outfile:
            dictionaryToJson = json.dump(playerStat, outfile)
        url = os.path.abspath(inspect.getfile(inspect.currentframe()))
        url = url[0:len(url)-9] + "2\index.htm"
        webbrowser.open(url,new=2)

    def lose(self, j):
        clear()
        print("nul.")
        input()

# tests
if __name__ == "__main__":
    from joueur import *
    v = View()
    j = Joueur("TestBot", 1)
    # Quel Object test :
    print( "Choix : ", v.quelObjet(["Test 1","Test 2","Test 3","Test 4","Test 5"]))
    input()
    # Experience display :
    for i in range(0,11):
        j.experience = i

        v.displayJoueur(j)
        print(i)
        input()

    v.win(j)
