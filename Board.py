import Point
import Object
import Rect
import Board
import Util
import ConstParam as cc

class Board():
    def __init__(self, lt, rb) :
        self.rect = Rect.Rect(lt, rb)
        self.pin = []
        for i in range(0, self.getWidth() * self.getHeight()) :
            self.pin.append(0);

    def drawPins(self) :
        for i in range(0, self.getHeight()) :
            Util.gotoxy(self.rect.LeftTop + Point.Point(0, i))
            for j in range(0, self.getWidth()) :
                if(self.pin[i*self.getWidth() + j] == 1) :
                    print(cc.cPin, end='')
                else :
                    print(cc.cEmpty, end='')
    
    def isPinsTouched(self, obj) :
        for i in range(0, 4) :
            offsetFromLT = obj.locate + obj.blocks[i] - self.rect.LeftTop
            idx = offsetFromLT.y * self.getWidth() + offsetFromLT.x
            if(self.pin[int(idx)] == 1) :
                return True
        
        return False

    def setObjectPins(self, obj) :
        for i in range(0, 4) :
            offsetFromLT = obj.locate + obj.blocks[i] - self.rect.LeftTop
            idx = offsetFromLT.y * self.getWidth() + offsetFromLT.x
            self.pin[int(idx)] = 1

    def lineCheckAndRearrange(self) :
        isFull = []
        downCounter = []
        for i in range(0, self.getHeight()) :
            isFull.append(True)
            downCounter.append(0)
        
        for i in range(0, self.getHeight()) :
            for j in range(0, self.getWidth()) :
                if(self.pin[i*self.getWidth() + j] == 0) :
                    isFull[i] = False
                    break
            
            if(isFull[i]) :
                for j in range(i-1, 0, -1) :
                    downCounter[j] = downCounter[j]+1
        
        tempPins = []
        for i in range(0, self.getWidth() * self.getHeight()) :
            tempPins.append(0);
        
        for i in range(0, self.getHeight()) :
            if (isFull[i] == False) :
                for j in range(0, self.getWidth()) :
                    idx = (i+downCounter[i]) * self.getWidth() + j
                    tempPins[idx] = self.pin[i*self.getWidth() + j]

        self.pin = tempPins

    def getRect(self) :
        return self.rect
    
    def getHeight(self) :
        return self.rect.height
    
    def getWidth(self) :
        return self.rect.width