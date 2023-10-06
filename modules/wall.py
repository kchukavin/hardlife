from modules.object import Object
import modules.constants as constants


class Wall(Object):
    type = constants.TYPE_WALL

    def __init__(self, x: int = 0, y: int = 0, color: tuple = constants.GRAY):
        super().__init__(x, y, color)
