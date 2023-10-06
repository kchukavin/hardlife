from modules.object import Object
from modules.constants import *


class Wall(Object):
    type = TYPE_WALL

    def __init__(self, x: int = 0, y: int = 0, color: tuple = GRAY):
        super().__init__(x, y, color)
