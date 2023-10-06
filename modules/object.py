import modules.constants as constants


class Object:
    type = constants.TYPE_OBJECT

    def __init__(self, x: int = 0, y: int = 0, color: tuple = constants.WHITE):
        self.x = x
        self.y = y
        self.color = color
        self.hp = constants.HP_DEFAULT

    def make_move(self):
        pass
