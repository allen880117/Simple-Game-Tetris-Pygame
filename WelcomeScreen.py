import pygame
import Util
from Point import *
import ConstParam as cp

class WelcomeScreen():
    def __init__(self) :
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(cp.ScreenSize)
        pygame.display.set_caption(cp.Title)
        
        # Text # Define
        self.text = pygame.font.Font(cp.font, 30)
        self.textList = []

        # Title Text
        TitleSurf = self.text.render(cp.SimpleTitle, True, (0,0,0), None)
        TitleRect = TitleSurf.get_rect()
        TitleRect.center = (cp.BoardWidth/2, cp.BoardHeight/2)
        self.textList.append((TitleSurf, TitleRect))

        # "Please Pres Any Key To Start"
        TitleSurf = self.text.render('Press any key to start', True, (0,0,0), None)
        TitleRect = TitleSurf.get_rect()
        TitleRect.center = (cp.BoardWidth/2, cp.BoardHeight/2 + cp.pixelHeight)
        self.textList.append((TitleSurf, TitleRect))

    def draw(self):
        # DRAW_TEXT
        Util.drawxy(Point = Point(0,0), Screen = self.screen, Width = 12, Height = 22, Color = (255, 255, 255))
        for text in self.textList :
            self.screen.blit(text[0], text[1])
        pygame.display.update()
                
        main_welcome_running = True
        while main_welcome_running :
            for event in pygame.event.get() :
                if event.type == pygame.KEYDOWN :
                    main_welcome_running = False