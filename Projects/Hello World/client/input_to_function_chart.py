from sprite import tank
from enum import Enum

class chart(Enum):

    UPDATE_SPEED = tank.update_speed
    SHOOT = tank.shoot
    AUTOSHOOT = tank.autoshoot
    ROTATE_CLOCKWISE = tank.rotate_clockwise
    ROTATE_ANTICLOCKWISE = tank.rotate_anticlockwise
    REORIENT = tank.reorient
