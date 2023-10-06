from modules.creature import Creature
import modules.constants as constants
import modules.field as Field

class Player(Creature):
    def __init__(self, field: Field, x: int=0, y: int=0, color: tuple=constants.WHITE):
        super().__init__(field, x, y, color)
        self.desire_to_move = None

    def want_to_move_to(self, direction: str):
        self.desire_to_move = direction

    def make_move(self):
        self.try_to_move(self.desire_to_move)
