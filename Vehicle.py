from Position import Position

class Vehicle:
    def __init__(self):
        self.position_p = Position(0,0,0)
        self.position_h = Position(1,0,0)
        self.speed = 0
        self.fracIndex = 0
