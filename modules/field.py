import random

from modules.constants import *
import modules.direction as direction
from .object import Object


class Field:
    def __init__(self):
        self.field = []
        self.objects = []
        for y in range(FIELD_HEIGHT):
            self.field.append([])
            for x in range(FIELD_WIDTH):
                self.field[y].append([])

    def add_object(self, object:Object) -> None:
        x = object.x
        y = object.y
        self.objects.append(object)
        self.field[y][x].append(object)

    def remove_object(self, object:Object) -> None:
        x = object.x
        y = object.y
        if self.field[y][x].count(object):
            self.field[y][x].remove(object)
        if self.objects.count(object):
            self.objects.remove(object)
            del object

    def move_object(self, object:Object, new_x:int, new_y:int) -> None:
        x = object.x
        y = object.y
        if self.field[y][x].count(object):
            self.field[y][x].remove(object)
        object.x = new_x
        object.y = new_y
        self.field[new_y][new_x].append(object)

    def is_empty(self, x:int, y:int) -> bool:
        return not bool(self.get_cell_content(x, y))

    def is_free(self, x:int, y:int, dir:int=direction.DIRECTION_NONE) -> bool:
        new_x = direction.get_new_x(x, dir)
        new_y = direction.get_new_y(y, dir)
        if (new_x < 0 or new_x >= FIELD_WIDTH
                or new_y < 0 or new_y >= FIELD_HEIGHT):
            return False

        if self.is_cell_has_type(new_x, new_y, TYPE_WALL) or self.is_cell_has_type(new_x, new_y, TYPE_CREATURE):
            return False

        return True

    def find_object_by_type(self, x:int, y:int, type:int) -> Object:
        for object in self.get_cell_content(x, y):
            if object.type == type:
                return object

        return None

    def is_cell_has_type(self, x:int, y:int, type:int) -> bool:
        return bool(self.find_object_by_type(x, y, type))

    def get_cell_content(self, x:int, y:int) -> list:
        if (x < 0 or x >= FIELD_WIDTH
                or y < 0 or y >= FIELD_HEIGHT):
            return []
        return self.field[y][x]

    def get_objects(self) -> list:
        return self.objects

    def print_field(self):
        print('\n'.join(['\t'.join([str(cell) for cell in row])
              for row in self.field]))
