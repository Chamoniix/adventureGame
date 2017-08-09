# -*-coding:Latin-1 -*

from map import *
import math

class Joueur:
    def __init__(self, nom, diff):
        self.name = nom
        self.hpMax = 100
        self.hp = 100
        self.attack = 10
        self.niveau = 1
        self.experience = 0
        self.upMsg = ""
        self.xpNeed = 10
        self.x = 0
        self.y = 0
        self.light = 3
        self.agroDist = 2
        if diff == 1:
            self.diff = "Facile"
            self.mapSize = 4
        elif diff == 2:
            self.diff = "Moyen"
            self.mapSize = 7
        elif diff == 3:
            self.diff = "Dur"
            self.mapSize = 10
        self.map = Map(self.mapSize, self.mapSize)
        self.map.setCell(self.x, self.y,'x')
        self.objs = []

    def act(self, instruct):
        msg = ""
        if instruct == 'n' or instruct == 's' or instruct == 'e' or instruct == 'w':
            res, msg = self.moove(instruct)
        elif instruct == 'd':
            res = self.down()
        elif instruct == 't':
            res, msg = self.take()
        self.testExp()
        return res, msg, self.upMsg

    def down(self):
        if self.isOut() == 0:
            lvl = self.map.lvl
            self.experience += (-lvl+1) * 4
            del self.map
            self.map = Map(self.mapSize - lvl + 1 , self.mapSize - lvl + 1 , lvl-1)
            self.map.setCell(self.x, self.y,'x')
            return 2
        else:
            return -2


    '''
    returns :
        -1 : You can't move this way
        +3 : You mooved, and get agro by a mob msg = x,y to identify the mob
        +0 : You mooved, nothing happened
    '''
    def moove(self, dir):
        msg = ""
        self.moveMobs()
        if (self.isOut() == 0):
            self.map.setCell(self.x,self.y,'o')
        elif (self.isOnObj() == 0):
            self.map.setCell(self.x,self.y,'#')
        else:
            self.map.setCell(self.x,self.y,'.')
        inix = self.x
        iniy = self.y
        if dir == "n":
            self.y += 1
        elif dir == "e":
            self.x += 1
        elif dir == "s":
            self.y -= 1
        elif dir == "w":
            self.x -= 1
        res = self.map.setCell(self.x,self.y,'x')
        if res < 0:
            self.x = inix
            self.y = iniy
            self.map.setCell(self.x,self.y,'x')
            return -1, "Out of range"
        else:
            res, msg = self.detectMob()
            if res == 0:
                return 3, msg #Mob found
            return 0, "You mooved, no mob"
    ''' returns :
        -3 : Not on an Object
        +1 : Took one object, msg = "OBJobjectname"
    '''
    def take(self):
        if self.isOnObj():
            return -3, ""
        else:
            self.map.obj.x = -1
            self.map.obj.y = -1
            nom = self.map.obj.nom
            self.objs.append(nom)

            if nom == "Torche":
                self.light +=1
            if nom == "Fireball":
                self.light +=3
            if nom == "Epe en bois":
                self.attack +=5
            if nom == "Epe en fer":
                self.attack +=15
            if nom == "Epe du demon":
                self.attack +=50
            if nom == "Petite Armure":
                self.hp +=10
                self.hpMax += 10
            if nom == "Grosse Armure":
                self.hp +=25
                self.hpMax += 25
            if nom == "Bouclier":
                self.hp +=20
                self.hpMax += 20
            if nom == "Masque":
                self.agroDist +=1

            self.experience += 10
            nom = "OBJ" + nom
            return 1,nom

    def moveMobs(self):
        for i in range(0,len(self.map.mobs)):
            j = 0
            while 1 :
                j += 1
                x = self.map.mobs[i].pos.x
                y = self.map.mobs[i].pos.y

                res = self.map.mobs[i].move(self.map)
                if (not self.map.getCell(self.map.mobs[i].pos.x,self.map.mobs[i].pos.y) == '.') or (res == -1):
                    self.map.mobs[i].setPos(Point(x,y))
                else:
                    self.map.setCell(x, y, '.')
                    self.map.setCell(self.map.mobs[i].pos.x, self.map.mobs[i].pos.y, '@')
                    break
                '''200 impossible moves, we can suppose the mob is stuck'''
                if j > 200:
                    break

    ''' Returns :
        -1 : No mob
        +0 : Mob, msg = x,y to identify the mob
        '''
    def detectMob(self):
        #Go thought all the map and consider only close enought cells
        for i in range (0,self.map.size.y):
            for k in range(0,self.map.size.x):
                if (abs(self.x - k) + abs((self.map.size.y-1 - self.y) - i)) <= self.agroDist:
                    if self.map.map[i][k] == "@":
                        msg = str(k) + "," + str(self.map.size.y-1-i)
                        return 0, msg
        return -1, "No Mob"


    ''' Returns :
        +0 : LVL UP
        -1 : same lvl as before
        '''
    def testExp(self):
        if self.experience > self.xpNeed :
            self.niveau += 1
            hp = random.randint(2,8)
            self.hp += hp
            self.hpMax += hp
            atk = random.randint(2,8)
            self.attack += atk
            if self.niveau == 5 :
                self.light += 1
                atk += ", LIGHT +1"
            self.xpNeed = 2 * math.pow(2, self.niveau-1) * 10
            self.upMsg = "LEVEL UP ! HP +" + str(hp) + ", ATK +" + str(atk)
            return 0
        else:
            self.upMsg= ""
            return -1


    def isOut(self):
        if self.x == self.map.out.x and self.y == self.map.out.y:
            return 0
        else:
            return -1

    def isOnObj(self):
        if self.x == self.map.obj.x and self.y == self.map.obj.y:
            return 0
        else:
            return -1

# tests
if __name__ == "__main__":
    print ("TODO : TEST")
