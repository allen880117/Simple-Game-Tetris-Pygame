from Point import *
from Rect import *

class Board():
    def __init__(self, LeftTop, Width, Height) :
        self.rect = Rect(LeftTop = LeftTop, Width = Width, Height = Height)
        self.pins = []
        for i in range(0, self.rect.width * self.rect.height) :
            self.pins.append(0)
    
    def PositionBoardPins(self) :
        Positions = []
        for i in range(0, self.rect.height) :
            for j in range(0, self.rect.width) :
                if self.pins[i*self.rect.width + j] == 1 :
                    Positions.append(self.rect.lefttop + Point(j, i))
        
        return Positions

    def setPinsByBlock(self, obj) :
        BlockList = obj.PositionBlocks()
        for Block in BlockList :
            Block = Block - self.rect.lefttop
            idx_for_pins = Block.y * self.rect.width + Block.x
            self.pins[int(idx_for_pins)] = 1

    def checkLineAndRearrange(self) :
        isFull = []
        downCounter = []
        for i in range(self.rect.height):
            isFull.append(False)
            downCounter.append(0)
        
        tempPins = []
        for i in range(0, self.rect.width * self.rect.height) :
            tempPins.append(0)

        for i in range(0, self.rect.height) :
            isLine = True
            for j in range(0, self.rect.width) :
                if self.pins[i*self.rect.width + j] == 0 :
                    isLine = False
                    break
            
            if isLine == True :
                isFull[i] = True
                for j in range(0, i) :
                    downCounter[j] = downCounter[j] + 1
        
        for i in range(0, self.rect.height) :
            if isFull[i] == True : continue

            for j in range(0, self.rect.width) :
                idx_for_orig = i*self.rect.width + j
                idx_for_temp = (i+downCounter[i]) *self.rect.width + j
                tempPins[idx_for_temp] = self.pins[idx_for_orig]

        self.pins = tempPins

    def isPinsTouchedByObj(self, obj) : 
        BlockList = obj.PositionBlocks()
        isTouched = False
        for Block in BlockList :
            Block = Block - self.rect.lefttop
            idx_for_pins = Block.y * self.rect.width + Block.x
            if self.pins[int(idx_for_pins)] == 1 :
                isTouched = True
                break
        
        return isTouched