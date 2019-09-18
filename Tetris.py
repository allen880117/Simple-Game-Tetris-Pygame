import pygame, random
import Util
from Point import *
from Rect import *
from Object import *
from Board import *
from PauseScreen import *
import ConstParam as cp

class Tetris():
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(cp.ScreenSize)
        pygame.display.set_caption(cp.Title)

        self.mainBoard = Board(LeftTop = Point(1, 1), Width = 10, Height = 20)
        self.generatePoint = self.mainBoard.rect.lefttop + Point(self.mainBoard.rect.width/2 -2, 0)
        self.RandType = random.randint(0, 6)
        self.block = Object(Type = self.RandType, Locate = self.generatePoint)
        self.shadow = Object(Type = self.RandType, Locate = self.generatePoint)

        self.BoundaryList = self.mainBoard.rect.PositionOuterBoundary()
        self.PinsList = []
        self.BlocksList = []
        self.ShadowBlocksList = []

        # Text
        self.text = pygame.font.Font(cp.font, 30)
        self.textSurf = self.text.render('TETRIS', True, (0,0,0), None)
        self.textRect = self.textSurf.get_rect()
        self.textRect.center = (cp.Width/2, cp.Height/2)

    def shadowMove(self):
        self.shadow.reset(Type = self.block.type, Locate = self.block.locate, Direction = self.block.direction)
        while (self.shadow.move(Point(0, 1), self.mainBoard)) : pass    

    def draw(self) :
        # SHADOW
        self.shadowMove() # SHADOW

        # DRAW
        self.PinsList = self.mainBoard.PositionBoardPins()
        self.ShadowBlocksList = self.shadow.PositionBlocks()
        self.BlocksList = self.block.PositionBlocks()

        # DRAW_BACKGROUND
        Util.drawxy(Point = Point(0,0), Screen = self.screen, Width = 12, Height = 22, Color = (255, 255, 255))
        
        # DRAW_TEXT
        self.screen.blit(self.textSurf, self.textRect)

        # DRAW_BLOCKS
        for pos in self.BoundaryList : Util.drawxy(Point = pos, Screen = self.screen, Color = (0, 0, 0))
        for pos in self.PinsList : Util.drawxy(Point = pos, Screen = self.screen, Color = (125, 0, 0))
        for pos in self.ShadowBlocksList : Util.drawxy(Point = pos, Screen = self.screen, Color = (125, 125, 125), Fill = 0)
        for pos in self.BlocksList : Util.drawxy(Point = pos, Screen = self.screen, Color = (0, 0, 125))
        
        pygame.display.update()

    def play(self) :
        main_game_running = True
        while main_game_running:

            self.RandType = random.randint(0, 6)
            self.block.reset(Type = self.RandType, Locate = self.mainBoard.rect.lefttop + Point(self.mainBoard.rect.width/2 -2, 0))
            if(self.mainBoard.isPinsTouchedByObj(self.block) == True) :
                main_game_running = False

            self.draw()
            
            BottomTouchCounter = 0

            while main_game_running:
                
                self.clock.tick(cp.FPS)
                emptyEvent = True
                
                for event in pygame.event.get() :
                    if event.type == pygame.QUIT :
                        return 1 # Directly Shut Down
                    elif event.type == pygame.KEYDOWN :
                        emptyEvent = False
                        if event.key == pygame.K_UP :
                            self.block.turn(SpinDirection = "CLOCKWISE", board = self.mainBoard)
                        elif event.key == pygame.K_DOWN :
                            self.block.move(Point(0,1), self.mainBoard)
                        elif event.key == pygame.K_LEFT :
                            self.block.move(Point(-1, 0), self.mainBoard)               
                        elif event.key == pygame.K_RIGHT :
                            self.block.move(Point(1, 0), self.mainBoard)               
                        elif event.key == pygame.K_SPACE :
                            while (self.block.move(Point(0, 1), self.mainBoard)) : pass    
                            BottomTouchCounter = cp.BottomCount           
                        elif event.key == pygame.K_ESCAPE :
                            # Initial Pause Screen
                            pauseScreen = PauseScreen(self.screen)
                            returnValue = pauseScreen.draw()
                            if returnValue == 1 :
                                return 1 # Directly Shut Down
                            # Restore the Screen
                            self.draw()
                        else:
                            self.block.move(Point(0, 1), self.mainBoard) 

                if emptyEvent == True : # Non Event Happen
                    self.block.move(Point(0, 1), self.mainBoard)   
                
                if self.block.isDownEnable(self.mainBoard) == True :
                    BottomTouchCounter = 0
                else :
                    BottomTouchCounter = BottomTouchCounter + 1
                
                if BottomTouchCounter >= cp.BottomCount :
                    self.mainBoard.setPinsByBlock(self.block)
                    self.mainBoard.checkLineAndRearrange()
                    self.draw()
                    break

                self.draw()
        
        return 0
