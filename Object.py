from Point import *
from BlockType import *
from Board import *

class Object():
    def __init__(self, Type, Locate, Direction = 0):
        self.reset(Type, Locate, Direction)

    def reset(self, Type, Locate, Direction = 0):
        self.type = Type
        self.locate = Locate
        self.direction = Direction
        self.offsets = [0, 1, 2, 3]

        self.switchTypeOrRotation()

    def switchTypeOrRotation(self):
        self.offsets = Block_Series[(int(self.type))%7][self.direction]
    
    def PositionBlocks(self):
        Positions = []
        for i in range(0, 4) :
            Positions.append(self.locate + self.offsets[i])
        
        return Positions
    
    def move(self, move_offset, board: Board): 
        self.locate = self.locate + move_offset
        isLegal = self.isInside(board) == True and board.isPinsTouchedByObj(self) == False
        if isLegal == False :
            self.locate = self.locate - move_offset
            return False
        else :
            return True

    def turn(self, board):
        self.direction = (self.direction+1)%4
        self.switchTypeOrRotation()

        isLegal = self.isInside(board) == True and board.isPinsTouchedByObj(self) == False
        if isLegal == False :
            self.direction = (self.direction-1+4)%4
            self.switchTypeOrRotation()
            return False
        else :
            return True

    def isInside(self, board: Board): 
        BlockList = self.PositionBlocks()
        isInside = True
        for Block in BlockList :
            if ( Block.x < board.rect.lefttop.x or
                 Block.x > board.rect.lefttop.x + board.rect.width-1 or
                 Block.y < board.rect.lefttop.y or 
                 Block.y > board.rect.lefttop.y + board.rect.height-1 ) :
                isInside = False
                break
        
        return isInside

    def isDownEnable(self, board: Board):
        if self.move(Point(0, 1), board) == False :
            return False
        else :
            self.move(Point(0, -1), board)
            return True
