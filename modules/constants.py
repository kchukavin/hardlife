FPS = 30  # Frame per second
TPS = 5  # Turn per second
FOOD_SPAWN_PERIOD = 10 # Turns

# Field
FIELD_WIDTH = 50
FIELD_HEIGHT = 50

# Cell
CELL_WIDTH = 16
CELL_HEIGHT = 16

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Object types
TYPE_OBJECT, TYPE_WALL, TYPE_CREATURE, TYPE_FOOD = range(4)

# Desires
DESIRE_NONE, DESIRE_EAT, DESIRE_REP = range(3)

# Actions
ACTION_EAT = range(1)

# Settings
HP_DEFAULT = 100.0
