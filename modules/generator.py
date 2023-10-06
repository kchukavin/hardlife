import random

from .constants import *
from .field import Field
from .wall import Wall
from .food import Food
from .creature import Creature


class Generator:
    def __init__(self, field: Field) -> None:
        self.field = field

    def generate_walls(self, count:int) -> None:
        for _ in range(count):
            x = random.randint(0, FIELD_WIDTH - 1)
            y = random.randint(0, FIELD_HEIGHT - 1)
            if self.field.is_free(x, y):
                self.field.add_object(Wall(x, y))

    def generate_food(self, count:int) -> None:
        for _ in range(count):
            x = random.randint(0, FIELD_WIDTH - 1)
            y = random.randint(0, FIELD_HEIGHT - 1)
            if self.field.is_free(x, y):
                self.field.add_object(Food(x, y))

    def generate_creatures(self, count:int) -> None:
        for _ in range(count):
            x = random.randint(0, FIELD_WIDTH - 1)
            y = random.randint(0, FIELD_HEIGHT - 1)
            if self.field.is_free(x, y):
                self.field.add_object(Creature(self.field, x, y))
