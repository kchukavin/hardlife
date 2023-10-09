from modules.object import Object
from modules.constants import *
import modules.field as Field


class Wall(Object):
    type = TYPE_WALL

    def __init__(self, field: Field, x: int = 0, y: int = 0, color: tuple = GRAY):
        super().__init__(field, x, y, color)
