data = {

    0 : {
        "name" : "test_tank",
        "health" : 100,
        "max_speed" : 1,
        "field_of_view" : 250,
        "colour" : (0, 0, 255),
        "radius" : 15,

        "linked_turret" : 1,
        "bullet_type" : {
            # The bullet would inherit color from the tank.
            # The speed is the relative speed of the bullet. When a bullet is fired, the absolute speed would be determined by the speed of tank and orientation
            "speed" : 0.5,
            "damage" : 10,
            "radius" : 3,
            },
        },

    1 : {
        "name" : "test_bullet_turret",
        "linked_type" : 0,
        "colour" : (125, 125, 125),
        "length" : 25,               ## From centre of tank
        "width" : 10,

        "health" : None,
        "max_speed" : None,
        "radius" : None,
        },

    101 : {
        "name" : "square",
        "health" : 10,
        "colour" : (255, 255, 0),
        "radius" : 5,
        },

    102 : {
        "name" : "triangle",
        "health" : 25,
        "colour" : (255, 0, 0),
        "radius" : 8,
        },

    }
