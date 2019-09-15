from getkey import getkey, keys

class Command:
    def __init__(self):
        self.keyType = -1
    
    def getInput(self):
        k = getkey(blocking=False)
        if k == keys.UP :
            self.keyType = 0
        elif k == keys.DOWN :
            self.keyType = 1
        elif k == keys.LEFT :
            self.keyType = 2
        elif k == keys.RIGHT :
            self.keyType = 3
        elif k == keys.ESC :
            self.keyType = 4
        elif k == keys.SPACE :
            self.keyType = 5
        else :
            self.keyType = -1
            
    def reset(self):
        self.keyType = -1