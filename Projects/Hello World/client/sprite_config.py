data = {

    0 : {
        "name" : "test_tank",
        "health" : 100,
        "max_speed" : 1,
        "field_of_view" : 250,
        "colour" : (0, 0, 255),
        "radius" : 15,
        "bullet_type" : 201,
        },

    1 : {
        "name" : "square",
        "health" : 10,
        "colour" : (255, 255, 0),
        "radius" : 5,
        },

    2 : {
        "name" : "triangle",
        "health" : 25,
        "colour" : (255, 0, 0),
        "radius" : 8,
        },

    # Configurations for the bullet are stored from 201 onwards
    201 : {
            # The bullet would inherit color from the tank.
            # The speed is the relative speed of the bullet. When a bullet is fired, the absolute speed would be determined by the speed of tank and orientation
            "speed" : 0.5,
            # Here the health field corrosponds to the damage. This is because a general sprite object doesnot have a property knaown as damage
            "health" : 10,
            "radius" : 3,
            "max_speed" : 1,
    }

    }
