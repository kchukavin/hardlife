from modules.object import Object
import modules.constants as constants


class Food(Object):
    type = constants.TYPE_FOOD

    def __init__(self, x: int = 0, y: int = 0, color: tuple = constants.GREEN):
        super().__init__(x, y, color)
