import pygame
import ConstParam as cp

def drawxy(**kwargs) :
    if kwargs.__contains__("Point") :
        x = kwargs["Point"].x
        y = kwargs["Point"].y
    elif kwargs.__contains__("X") and kwargs.__contains__("Y") :
        x = kwargs["X"]
        y = kwargs["Y"]
    else:
        x = 0
        y = 0
    
    if kwargs.__contains__("Width") :
        width = kwargs["Width"] * cp.pixelWidth
    else:
        width = cp.pixelWidth

    if kwargs.__contains__("Height") :
        height = kwargs["Height"] * cp.pixelHeight
    else:
        height = cp.pixelHeight

    if kwargs.__contains__("Color") :
        color = kwargs["Color"] 
    else:
        color = cp.ColorBlack

    if kwargs.__contains__("Fill") :
        fill = kwargs["Fill"]
    else:
        fill = 0 

    pygame.draw.rect(kwargs["Screen"], color, (x*cp.pixelWidth, y*cp.pixelHeight, width, height), fill)