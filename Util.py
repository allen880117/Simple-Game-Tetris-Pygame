import os
import platform
import time
import Point
import ConstParam as cc

def clrscr():
    if platform.system() == 'Windows' :
        os.system("cls")
    elif platform.system() == 'Linux' :
        os.system("clear")

def gotoxy(*args):
    if type(args[0]) == Point.Point :
        x = args[0].x
        y = args[0].y
    elif len(args) == 2 :
        x = args[0]
        y = args[1]
    else :
        x = 0
        y = 0
        
    print ("%c[%d;%df" % (0x1B, y, x * cc.scaleWidth ), end='')

def delay(second):
    print ('')
    #print ("Start : %s" % time.ctime())
    time.sleep(second)
    print ('')
    #print ("End : %s" % time.ctime())

    # It's is weird that I can't successfully run "sleep"
    # without printing 'endl'