import random

from modules.object import Object
import modules.constants as constants
import modules.direction as direction
import modules.field as Field


class Creature(Object):
    type = constants.TYPE_CREATURE

    def __init__(self, field: Field, x: int = 0, y: int = 0, color: tuple = constants.RED):
        super().__init__(x, y, color)
        self.field = field
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

    def make_move(self):
        self.try_to_move(random.choice(direction.ALL_DIRECTIONS))