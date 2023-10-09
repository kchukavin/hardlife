from modules.object import Object
from modules.constants import *
import modules.field as Field


class Food(Object):
    type = TYPE_FOOD

    def __init__(self, field: Field, x: int = 0, y: int = 0, color: tuple = GREEN):
        super().__init__(field, x, y, color)
