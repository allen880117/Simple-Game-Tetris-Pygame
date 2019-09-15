import Rect

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # + overload
    def __add__(self, rhs):
        return Point(self.x+rhs.x, self.y+rhs.y)
    
    # - overload
    def __sub__(self, rhs):
        return Point(self.x-rhs.x, self.y-rhs.y)

    def isInside(self, rect):
        return rect.contains(self)

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y        

    def show(self, endChar = ''):
        print("x = %d y = %d" % (self.x, self.y) , end = endChar);
    