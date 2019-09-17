from Point import *

class Rect():
    def __init__(self, LeftTop, Width, Height):
        self.lefttop = LeftTop
        self.width = Width
        self.height = Height

    def PositionOuterBoundary(self):
        Positions = []
        for i in range(0, self.width+2) :
            Positions.append(self.lefttop+Point(-1, -1)+Point(i, 0))
        for i in range(1, self.height+2-1):
            Positions.append(self.lefttop+Point(-1, -1)+Point(0, i))
            Positions.append(self.lefttop+Point(self.width, -1)+Point(0, i))
        for i in range(0, self.width+2) :
            Positions.append(self.lefttop+Point(-1, self.height)+Point(i, 0))

        return Positions
