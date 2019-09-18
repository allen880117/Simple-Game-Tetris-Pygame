from Point import *
from BlockType import *
from KickTable import *
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

    def turn(self, SpinDirection, board):
        orig_direction = self.direction
        orig_locate = self.locate

        if SpinDirection == "CLOCKWISE" :
            self.direction = (self.direction+1)%4
            self.switchTypeOrRotation()
        elif SpinDirection == "COUNTERCLOCKWISE" :
            self.direction = (self.direction-1+4)%4
            self.switchTypeOrRotation()
        
        TestCounter = 0
        isLegal = False        
        while isLegal == False and TestCounter < 5 :
            self.kick(OriginDirection = orig_direction, SpinDirection = SpinDirection, TestTime = TestCounter)
            isLegal = self.isInside(board) == True and board.isPinsTouchedByObj(self) == False
            TestCounter = TestCounter + 1

        if isLegal == False :
            self.direction = orig_direction
            self.switchTypeOrRotation()

            self.locate = orig_locate
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

    def kick(self, OriginDirection, SpinDirection, TestTime):
        if SpinDirection == "CLOCKWISE" :
            self.locate = self.locate + KICK_CLOCKWISE[self.type][OriginDirection][TestTime]
        elif SpinDirection == "COUNTERCLOCKWISE":
            self.locate = self.locate + KICK_COUNTERCLOCKWISE[self.type][OriginDirection][TestTime]