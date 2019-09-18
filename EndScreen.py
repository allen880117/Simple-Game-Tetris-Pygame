import pygame
import Util
from Point import *
import ConstParam as cp

class EndScreen():
    def __init__(self) :
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(cp.ScreenSize)
        pygame.display.set_caption(cp.Title)

        # Text
        self.text = pygame.font.Font(cp.font, 30)
        self.textSurf = self.text.render('GAME OVER', True, (0,0,0), None)
        self.textRect = self.textSurf.get_rect()
        self.textRect.center = (cp.Width/2, cp.Height/2)

    def draw(self):
        # DRAW_TEXT
        Util.drawxy(Point = Point(0,0), Screen = self.screen, Width = 12, Height = 22, Color = (255, 255, 255))
        self.screen.blit(self.textSurf, self.textRect)
        pygame.display.update()
                
        main_welcome_running = True
        while main_welcome_running :
            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_UP :
                        main_welcome_running = False
                    else :
                        return True
        
        return False