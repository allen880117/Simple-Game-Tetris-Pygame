import pygame
import Util
from Point import *
import ConstParam as cp

# Basically this PauseScreen have to be embedded in class Tetris
class PauseScreen():
    def __init__(self, screen) :
        self.clock = pygame.time.Clock()
        self.screen = screen

        # Text
        self.text = pygame.font.Font(cp.font, 30)
        self.textSurf = self.text.render('PAUSE', True, cp.ColorBlack, cp.ColorWhite)
        self.textRect = self.textSurf.get_rect()
        self.textRect.center = (cp.Width/2, cp.Height/2 + cp.pixelHeight)

    def draw(self):
        # DRAW_TEXT
        self.screen.blit(self.textSurf, self.textRect)
        pygame.display.update()
                
        pause_running = True
        while pause_running :
            for event in pygame.event.get() :
                if event.type == pygame.QUIT :
                    return 1
                elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_ESCAPE :
                        pause_running = False 
                        return 0 # Back to Process of Tetris
        
        # Safely Back to Main Process of Tetris
        return 0