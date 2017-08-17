# -*-coding:Latin-1 -*

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def delete(self):
        self.x = -1
        self.y = -1
