import random
import math

from .object import Object
from modules.constants import *
import modules.direction as direction
from .field import Field
from .sound import Sound


class Creature(Object):
    type = TYPE_CREATURE

    def __init__(self, field: Field, x: int = 0, y: int = 0, color: tuple = RED):
        super().__init__(field, x, y, color)
        self.desire = DESIRE_NONE
        self.desire_to_move = None
        self.sound = Sound()

    def __del__(self):
        self.sound.play_die()

    def determine_desire(self) -> int:
        if self.hp < 50:
            return DESIRE_EAT
        elif self.hp < 70:
            return DESIRE_REP

        return DESIRE_NONE

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
            to_eat = min(HP_DEFAULT - self.hp, food.hp)
            self.hp += to_eat
            food.hp -= to_eat
            self.sound.play_eat()

    def try_to_reproduce(self, dir: int) -> None:
        if self.hp <= 50:
            return

        subject = self.field.find_object_by_type(direction.get_new_x(
            self.x, dir), direction.get_new_y(self.y, dir), TYPE_CREATURE)

        if not subject or subject == self or subject.hp <= 50:
            return

        self.hp -= 20
        subject.hp -= 20
        new_creature = Creature(self.field, self.x, self.y, self.color)
        new_creature.hp = 50
        self.field.add_object(new_creature)
        self.sound.play_rep()

    def make_turn(self):
        super().make_turn()
        self.make_move()
        self.hp -= 1

    def make_move(self):
        aim = None
        if self.determine_desire() == DESIRE_EAT:
            aim = self.find_closest_object(TYPE_FOOD)
        elif self.determine_desire() == DESIRE_REP:
            aim = self.find_closest_object(TYPE_CREATURE)

        if aim:
            self.make_desire_to_move_to_object(aim)
        else:
            self.desire_to_move = random.choice(direction.ALL_DIRECTIONS)

        self.try_to_reproduce(self.desire_to_move)

        if not self.field.is_free(self.x, self.y, self.desire_to_move):
            self.desire_to_move = random.choice(direction.ALL_DIRECTIONS)

        self.try_to_eat()
        self.try_to_move(self.desire_to_move)

    def find_closest_object(self, type: int) -> Object:
        closest_object = None
        shortest_dist = None
        for object in self.field.get_objects():
            if object.type != type:
                continue

            dist = math.dist([self.x, self.y], [object.x, object.y])
            if not shortest_dist or dist < shortest_dist:
                closest_object = object
                shortest_dist = dist

        return closest_object

    def make_desire_to_move_to_object(self, object: Object) -> None:
        for dir in direction.ALL_DIRECTIONS:
            dist_x = math.dist([self.x], [object.x])
            dist_y = math.dist([self.y], [object.y])
            if dist_x > dist_y:
                if math.dist([direction.get_new_x(self.x, dir)], [object.x]) < dist_x:
                    self.desire_to_move = dir
            else:
                if math.dist([direction.get_new_y(self.y, dir)], [object.y]) < dist_y:
                    self.desire_to_move = dir
