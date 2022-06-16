class Node:

    idNodeGlobal = 0

    def __init__(self, x, y):
        Node.idNodeGlobal += 1
        self.idNode = Node.idNodeGlobal
        self.x = x
        self.y = y
        self.g = 999999999
        self.h = 999999999
        self.f = 999999999
        self.parent = None

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getG(self):
        return self.g

    def setG(self, g):
        self.g = g

    def getH(self):
        return self.h

    def setH(self, h):
        self.h = h

    def getF(self):
        return self.f

    def setF(self, f):
        self.f = f

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def __str__(self):
        res = "ID : " + str(self.idNode)
        res += " | X : " + str(self.x) 
        res += " | Y : " + str(self.y)
        res += " | G : " + str(self.g)
        res += " | H : " + str(self.h)
        res += " | F : " + str(self.f)
        # res += " | Parent : " + str(self.parent)
        return res

    def __lt__(self, other):
        return self.f < other.f