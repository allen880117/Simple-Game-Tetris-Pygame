import pygame, random
import Util
from Point import *
from Rect import *
from Object import *
from Board import *
import ConstParam as cp

pygame.init()

screen = pygame.display.set_mode(cp.ScreenSize)
pygame.display.set_caption(cp.Title)
clock = pygame.time.Clock()

mainBoard = Board(LeftTop = Point(1, 1), Width = 10, Height = 20)
generatePoint = mainBoard.rect.lefttop + Point(mainBoard.rect.width/2 -2, 0)
RandType = random.randint(0, 6)
block = Object(Type = RandType, Locate = generatePoint)
shadow = Object(Type = RandType, Locate = generatePoint)

BoundaryList = mainBoard.rect.PositionOuterBoundary()
PinsList = []
BlocksList = []
ShadowBlocksList = []

def shadowMove():
    shadow.reset(Type = block.type, Locate = block.locate, Direction = block.direction)
    while (shadow.move(Point(0, 1), mainBoard)) : pass    

def draw() :
    # SHADOW
    shadowMove() # SHADOW

    # DRAW
    PinsList = mainBoard.PositionBoardPins()
    ShadowBlocksList = shadow.PositionBlocks()
    BlocksList = block.PositionBlocks()

    Util.drawxy(Point = Point(0,0), Screen = screen, Width = 12, Height = 22, Color = (255, 255, 255))
    for pos in BoundaryList : Util.drawxy(Point = pos, Screen = screen, Color = (0, 0, 0))
    for pos in PinsList : Util.drawxy(Point = pos, Screen = screen, Color = (125, 0, 0))
    for pos in ShadowBlocksList : Util.drawxy(Point = pos, Screen = screen, Color = (125, 125, 125), Fill = 0)
    for pos in BlocksList : Util.drawxy(Point = pos, Screen = screen, Color = (0, 0, 125))
    pygame.display.update()
    
def main() :
    main_game_running = True
    while main_game_running:

        RandType = random.randint(0, 6)
        block.reset(Type = RandType, Locate = mainBoard.rect.lefttop + Point(mainBoard.rect.width/2 -2, 0))
        if(mainBoard.isPinsTouchedByObj(block) == True) :
            main_game_running = False

        draw()
        
        BottomTouchCounter = 0

        while main_game_running:
            
            clock.tick(cp.FPS)
            emptyEvent = True
            
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    main_game_running = False 
                    break
                elif event.type == pygame.KEYDOWN :
                    emptyEvent = False
                    if event.key == pygame.K_UP :
                        block.turn(mainBoard)
                    elif event.key == pygame.K_DOWN :
                        block.move(Point(0,1), mainBoard)
                    elif event.key == pygame.K_LEFT :
                        block.move(Point(-1, 0), mainBoard)               
                    elif event.key == pygame.K_RIGHT :
                        block.move(Point(1, 0), mainBoard)               
                    elif event.key == pygame.K_SPACE :
                        while (block.move(Point(0, 1), mainBoard)) : pass    
                        BottomTouchCounter = cp.BottomCount           
                    elif event.key == pygame.K_ESCAPE :
                        main_game_running = False
                        break
                    else:
                        block.move(Point(0, 1), mainBoard) 

            if emptyEvent == True : # Non Event Happen
                block.move(Point(0, 1), mainBoard)   
            
            if block.isDownEnable(mainBoard) == True :
                BottomTouchCounter = 0
            else :
                BottomTouchCounter = BottomTouchCounter + 1
            
            if BottomTouchCounter >= cp.BottomCount :
                mainBoard.setPinsByBlock(block)
                mainBoard.checkLineAndRearrange()
                draw()
                break

            draw()
            

    pygame.quit()


if __name__ == "__main__":
    main()