import random
import Point
import Object
import Rect
import Board
import Command
import ConstParam as cc
import Util
import os

class Tetris():
    def __init__(self) :
        self.mainBoard = Board.Board(Point.Point(5,5), Point.Point(4+10,4+20))
        self.generatePoint = self.mainBoard.getRect().getLeftTop() + Point.Point(self.mainBoard.getWidth()/2 -2, 0)
        self.block = Object.Object(self.PROCESS_RNG(), self.generatePoint)
        self.command = Command.Command()
        self.BottomTouchCounter = 0
    
    def PROCESS_ALL(self) : 
        Util.clrscr()
        self.PROCESS_DRAW_BOUNDARY()

        while True :
            self.PROCESS_RESET_BTC()
            self.PROCESS_RESET_BLOCK()
            if self.PROCESS_CHECK_GENERATE() == False :
                self.PROCESS_END_GAME()
                return 0
            else :
                self.PROCESS_DRAW_BLOCK()
            
            while True :
                Util.delay(cc.delayTime)
                
                if self.PROCESS_KB_OPERATE() == 1 :
                    return 0 # END GAME
                
                self.PROCESS_CHECK_BTC_COUNT()

                if self.PROCESS_CHECK_BTC_TRIGGER() == True :
                    break

    def PROCESS_RNG(self) :
        return random.randint(0,6)
    
    def PROCESS_RESET_BTC(self) :
        self.BottomTouchCounter = 0
    
    def PROCESS_RESET_BLOCK(self) :
        self.block.reset(self.PROCESS_RNG(), self.generatePoint)
    
    def PROCESS_CHECK_GENERATE(self) :
        if self.block.isTouchPins(self.mainBoard) :
            Util.gotoxy(self.mainBoard.getRect().getRightBottom() + Point.Point(2, 0))
            print("GAME OVER", end='')
            return False
        else :
            return True
    
    def PROCESS_CHECK_BTC_COUNT(self) :
        if self.block.isDownEnable(self.mainBoard) == True:
            self.BottomTouchCounter = 0
        else :
            self.BottomTouchCounter = self.BottomTouchCounter +1
    
    def PROCESS_CHECK_BTC_TRIGGER(self) :
        if self.BottomTouchCounter >= 3 :
            self.block.draw(False)
            self.mainBoard.setObjectPins(self.block)
            self.mainBoard.lineCheckAndRearrange()

            # Util.setColor(4)
            self.mainBoard.drawPins()
            return True
        else :
            return False
        
    def PROCESS_DRAW_BOUNDARY(self) :
        # Util.setColor(10)
        self.mainBoard.getRect().drawOuterBoundary()
    
    def PROCESS_DRAW_BLOCK(self) :
        # Util.setColor(7)
        self.block.draw(True)
    
    def PROCESS_KB_OPERATE(self) :
        self.command.getInput()
        if self.command.keyType == 4 :
            self.PROCESS_END_GAME()
            return 1
        elif self.command.keyType ==  0:
            self.block.draw(False)
            self.block.turn("CLOCKWISE", self.mainBoard)
            self.block.draw(True)
        elif self.command.keyType == 1 :
            self.block.draw(False)
            self.block.move(Point.Point(0, 1), self.mainBoard)
            self.block.draw(True)
        elif self.command.keyType == 2 :
            self.block.draw(False)
            self.block.move(Point.Point(-1, 0), self.mainBoard)
            self.block.draw(True)
        elif self.command.keyType == 3 :
            self.block.draw(False)
            self.block.move(Point.Point(1, 0), self.mainBoard)
            self.block.draw(True)
        elif self.command.keyType == 5 :
            self.block.draw(False)
            while (self.block.move(Point.Point(0, 1), self.mainBoard)) : pass
            self.BottomTouchCounter = 3
            self.block.draw(True)
        else :
            self.block.draw(False)
            self.block.move(Point.Point(0, 1), self.mainBoard)
            self.block.draw(True)

        self.command.reset()
        return 0

    def PROCESS_END_GAME(self) :
        Util.gotoxy(self.mainBoard.getRect().getRightBottom() + Point.Point(2, 0))
        print("GAME OVER", end='')

        os.system("PAUSE")    
        
