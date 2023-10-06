from modules.constants import *


class Object:
    type = TYPE_OBJECT

    def __init__(self, x:int=0, y:int=0, color:tuple=WHITE):
        self.x = x
        self.y = y
        self.color = color
        self.hp = HP_DEFAULT

    def make_move(self):
        pass
