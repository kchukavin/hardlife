# Направления
DIRECTION_NONE, DIRECTION_UP, DIRECTION_RIGHT, DIRECTION_DOWN, DIRECTION_LEFT = range(5)

ALL_DIRECTIONS = (
    DIRECTION_UP,
    DIRECTION_RIGHT,
    DIRECTION_DOWN,
    DIRECTION_LEFT
)

def get_direction_dx(dir:int) -> int:
    if dir == DIRECTION_RIGHT:
        return 1
    elif dir == DIRECTION_LEFT:
        return -1
    return 0

def get_direction_dy(dir:int) -> int:
    if dir == DIRECTION_UP:
        return -1
    elif dir == DIRECTION_DOWN:
        return 1
    return 0

def get_new_x(x:int, dir:int) -> int:
    return x + get_direction_dx(dir)

def get_new_y(y:int, dir:int) -> int:
    return y + get_direction_dy(dir)
