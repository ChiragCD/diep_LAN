from sprite import tank
from enum import Enum

class chart(Enum):

    MOVE_UP = tank.move_up
    MOVE_DOWN = tank.move_down
    MOVE_LEFT = tank.move_left
    MOVE_RIGHT = tank.move_right

    SHOOT = tank.shoot
    AUTOSHOOT = tank.autoshoot
    ROTATE_CLOCKWISE = tank.rotate_clockwise
    ROTATE_ANTICLOCKWISE = tank.rotate_anticlockwise
