import Object
import Point
import Util
import ConstParam as cc

class Rect():
    def __init__(self, lt, rb):
        self.LeftTop = lt
        self.RightBottom = rb
        self.width = (rb-lt).x + 1
        self.height = (rb-lt).y + 1
    
    def contains(self, pt):
        if (type(pt) == Point.Point) :
            if(pt.x >= self.LeftTop.x and pt.x <= self.RightBottom.x and
            pt.y >= self.LeftTop.y and pt.y <= self.RightBottom.y ) :
                return True
        elif (type(pt) == Object.Object):
            if (
              self.contains(pt.locate + pt.blocks[0]) and
              self.contains(pt.locate + pt.blocks[1]) and
              self.contains(pt.locate + pt.blocks[2]) and              
              self.contains(pt.locate + pt.blocks[3]) ) :
                return True
        else :
            return False

    def drawOuterBoundary(self):
        Util.gotoxy(self.LeftTop + Point.Point(-1, -1))
        for i in range(0, self.width+2) :
            if( i==0 or i == self.width+2 - 1) :
                print(cc.cConner, end = '')
            else :
                print(cc.cDash, end = '')
        
        for i in range(1, self.height+2-1) :
            Util.gotoxy(self.LeftTop + Point.Point(-1, i-1))
            for j in range(0, self.width+2) :
                if( j == 0 or j == self.width+2 - 1) :
                    print(cc.cSideEdge, end = '')
                else :
                    print(cc.cEmpty, end = '')
        
        Util.gotoxy(self.LeftTop + Point.Point(-1, self.height))
        for i in range(0, self.width+2) :
            if( i==0 or i == self.width+2 - 1) :
                print(cc.cConner, end = '')
            else :
                print(cc.cDash, end = '')
        
        # Avoid the twinkle of cursor
        Util.gotoxy(0, 0);
    
    def getLeftTop(self):
        return self.LeftTop
    
    def getRightBottom(self):
        return self.RightBottom

