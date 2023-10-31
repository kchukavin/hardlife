from modules.constants import *
import modules.field as Field


class Object:
    type = TYPE_OBJECT

    def __init__(self, field: Field, x: int = 0, y: int = 0, color: tuple = WHITE):
        self.field = field
        self.x = x
        self.y = y
        self.color = color
        self.hp = HP_DEFAULT

    def make_turn(self):
        if self.hp <= 0:
            self.field.remove_object(self)

    def make_move(self):
        pass
