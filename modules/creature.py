import random

from modules.object import Object
from modules.constants import *
import modules.direction as direction
import modules.field as Field


class Creature(Object):
    type = TYPE_CREATURE

    def __init__(self, field: Field, x: int = 0, y: int = 0, color: tuple = RED):
        super().__init__(field, x, y, color)
        self.desire_to_move = None

    def move(self, dir: int):
        self.field.move_object(
            self,
            direction.get_new_x(self.x, dir),
            direction.get_new_y(self.y, dir)
        )

    def try_to_move(self, dir: int):
        if self.field.is_free(self.x, self.y, dir):
            self.move(dir)

    def try_to_eat(self):
        food = self.field.find_object_by_type(self.x, self.y, TYPE_FOOD)
        if food:
            self.hp += food.hp
            food.hp = 0

    def make_turn(self):
        super().make_turn()
        self.try_to_eat()
        self.hp -= 1

    def make_move(self):
        self.try_to_move(random.choice(direction.ALL_DIRECTIONS))
