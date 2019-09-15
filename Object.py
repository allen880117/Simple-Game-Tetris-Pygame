import Point
import Object
import Rect
import Board
import Util
import ConstParam as cc

class Object():

    def __init__(self, ty, loc) :
        self.type = ty
        self.direction = 0
        self.locate = loc
        self.blocks = [0,1,2,3]
        self.switchTypeDirection(self.type, self.direction)

    def switchTypeDirection(self, type, direction) :
        if self.type == 0 : # I
            if   self.direction == 0: self.setBlocks(Point.Point(0, 1), Point.Point(1, 1), Point.Point(2, 1), Point.Point(3, 1))
            elif self.direction == 1: self.setBlocks(Point.Point(2, 0), Point.Point(2, 1), Point.Point(2, 2), Point.Point(2, 3))
            elif self.direction == 2: self.setBlocks(Point.Point(0, 2), Point.Point(1, 2), Point.Point(2, 2), Point.Point(3, 2))
            elif self.direction == 3: self.setBlocks(Point.Point(1, 0), Point.Point(1, 1), Point.Point(1, 2), Point.Point(1, 3))
            else: self.setBlocks(Point.Point(0, 1), Point.Point(1, 1), Point.Point(2, 1), Point.Point(3, 1))
        elif self.type == 1 : # J
            if   self.direction == 0: self.setBlocks(Point.Point(0, 0), Point.Point(0, 1), Point.Point(1, 1), Point.Point(2, 1))
            elif self.direction == 1: self.setBlocks(Point.Point(1, 0), Point.Point(2, 0), Point.Point(1, 1), Point.Point(1, 2))
            elif self.direction == 2: self.setBlocks(Point.Point(2, 2), Point.Point(0, 1), Point.Point(1, 1), Point.Point(2, 1))
            elif self.direction == 3: self.setBlocks(Point.Point(1, 0), Point.Point(1, 1), Point.Point(1, 2), Point.Point(0, 2))
            else: self.setBlocks(Point.Point(0, 0), Point.Point(0, 1), Point.Point(1, 1), Point.Point(2, 1))
        elif self.type == 2: # L
            if   self.direction == 0: self.setBlocks(Point.Point(2, 0), Point.Point(0, 1), Point.Point(1, 1), Point.Point(2, 1))
            elif self.direction == 1: self.setBlocks(Point.Point(1, 0), Point.Point(1, 1), Point.Point(1, 2), Point.Point(2, 2))
            elif self.direction == 2: self.setBlocks(Point.Point(0, 2), Point.Point(0, 1), Point.Point(1, 1), Point.Point(2, 1))
            elif self.direction == 3: self.setBlocks(Point.Point(1, 0), Point.Point(1, 1), Point.Point(1, 2), Point.Point(0, 0))
            else: self.setBlocks(Point.Point(2, 0), Point.Point(0, 1), Point.Point(1, 1), Point.Point(2, 1))
        elif self.type == 3: # O
            self.setBlocks(Point.Point(1, 0), Point.Point(2, 0), Point.Point(1, 1), Point.Point(2, 1))
        elif self.type == 4: # S
            if   self.direction == 0: self.setBlocks(Point.Point(1, 0), Point.Point(2, 0), Point.Point(0, 1), Point.Point(1, 1))
            elif self.direction == 1: self.setBlocks(Point.Point(1, 0), Point.Point(1, 1), Point.Point(2, 1), Point.Point(2, 2))
            elif self.direction == 2: self.setBlocks(Point.Point(1, 1), Point.Point(2, 1), Point.Point(0, 2), Point.Point(1, 2))
            elif self.direction == 3: self.setBlocks(Point.Point(0, 0), Point.Point(0, 1), Point.Point(1, 1), Point.Point(1, 2))
            else: self.setBlocks(Point.Point(1, 0), Point.Point(2, 0), Point.Point(0, 1), Point.Point(1, 1))
        elif self.type == 5: # T
            if   self.direction == 0: self.setBlocks(Point.Point(1, 0), Point.Point(0, 1), Point.Point(1, 1), Point.Point(2, 1))
            elif self.direction == 1: self.setBlocks(Point.Point(1, 0), Point.Point(1, 1), Point.Point(2, 1), Point.Point(1, 2))
            elif self.direction == 2: self.setBlocks(Point.Point(1, 2), Point.Point(0, 1), Point.Point(1, 1), Point.Point(2, 1))
            elif self.direction == 3: self.setBlocks(Point.Point(0, 1), Point.Point(1, 0), Point.Point(1, 1), Point.Point(1, 2))
            else: self.setBlocks(Point.Point(1, 0), Point.Point(0, 1), Point.Point(1, 1), Point.Point(2, 1))
        elif self.type == 6: # Z
            if   self.direction == 0: self.setBlocks(Point.Point(0, 0), Point.Point(1, 0), Point.Point(1, 1), Point.Point(2, 1))
            elif self.direction == 1: self.setBlocks(Point.Point(2, 0), Point.Point(2, 1), Point.Point(1, 1), Point.Point(1, 2))
            elif self.direction == 2: self.setBlocks(Point.Point(0, 1), Point.Point(1, 1), Point.Point(1, 2), Point.Point(2, 2))
            elif self.direction == 3: self.setBlocks(Point.Point(1, 0), Point.Point(1, 1), Point.Point(0, 1), Point.Point(0, 2))
            else: self.setBlocks(Point.Point(0, 0), Point.Point(1, 0), Point.Point(1, 1), Point.Point(2, 1))
        else : # O
            self.setBlocks(Point.Point(1, 0), Point.Point(2, 0), Point.Point(1, 1), Point.Point(2, 1))


    def move(self, offset, board) :
        self.locate = self.locate + offset
        isLegal = (self.isInsideRect(board.getRect()) == True) and (self.isTouchPins(board)==False)
        if (isLegal == False) :
            self.locate =self.locate - offset
            return False
        else :
            return True    

    def turn(self, dirclock, board) :
        if(dirclock == "CLOCKWISE") :
            self.direction = 0 if (self.direction >= 3) else self.direction+1
        else :
            self.direction = 3 if (self.direction <= 0) else self.direction-1

        self.switchTypeDirection(self.type, self.direction)

        isLegal = (self.isInsideRect(board.getRect()) == True) and (self.isTouchPins(board)==False)

        if(isLegal == False) :
            if(dirclock == "CLOCKWISE") :
                self.direction = 3 if (self.direction <= 0) else self.direction-1
            else :
                self.direction = 0 if (self.direction >= 3) else self.direction+1
            
            self.switchTypeDirection(self.type, self.direction)
            return False
        
        else :
            return True

    def reset(self, type, loc) :
        self.type = type
        self.direction = 0
        self.locate = loc
        self.switchTypeDirection(self.type, self.direction)

    def isInsideRect(self, rect) :
        return rect.contains(self)
    
    def isTouchPins(self, board) :
        return board.isPinsTouched(self)
    
    def isDownEnable(self, board) :
        self.locate = self.locate + Point.Point(0, 1)
        isLegal = (self.isInsideRect(board.getRect()) == True) and (self.isTouchPins(board) == False)
        self.locate = self.locate - Point.Point(0, 1)
        return isLegal
    
    def draw(self, show) :
        for i in range(0, 4) :
            Util.gotoxy(self.locate + self.blocks[i])
            if(show == True) :
                print(cc.cBlocks, end = '')
            else :
                print(cc.cEmpty, end = '')
        
        # Avoid the twinkle of cursor
        Util.gotoxy(0, 0)
    
    def setBlocks(self, pt0, pt1, pt2, pt3) : 
        self.blocks[0] = pt0
        self.blocks[1] = pt1
        self.blocks[2] = pt2
        self.blocks[3] = pt3
