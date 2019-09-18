from Tetris import *
from WelcomeScreen import *
from EndScreen import *
import pygame 

def main() :
    welcome = WelcomeScreen()
    welcome.draw()

    while True :
        tetris = Tetris()
        returnValue = tetris.play()
        if returnValue == 1 : # Directly Shut Down
            break

        end = EndScreen()
        returnValue = end.draw()
        if returnValue == False :
            break

if __name__ == "__main__":
    pygame.init()
    main() 
    pygame.quit()
