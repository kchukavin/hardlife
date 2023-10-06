from modules.object import Object
from modules.constants import *


class Food(Object):
    type = TYPE_FOOD

    def __init__(self, x: int = 0, y: int = 0, color: tuple = GREEN):
        super().__init__(x, y, color)
