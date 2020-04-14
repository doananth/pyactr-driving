import math

class Position:
    def __init__(self, xArg, zArg):
        self.x = xArg
        self.y = 0
        self.z = zArg
        
    def add(self, l2 = Position(x, y, z)):
        return Position(l2.x + self.x, l2.z + self.z)

    def subtract(self, l2 = Position(x, y, z)):
        return Position(l2.x - self.x, l2.z - self.z)

    def scale(self, s = float(input())):
        return Position(s * self.x, s * self.z)

    def average(self, l2 = Position(x, y, z), weight = float(input())):
        return Position(((1.0-weight) * self.x) + (weight * l2.x), ((1.0 - weight) * self.z) + (weight * l2.z))

    def normalize(self):
        m = math.sqrt((self.x * self.x) + (self.z * self.z))
        return Position(self.x/m, self.z/m)

    def rotate(self, degrees = float(input())):
        angle = (-180 * (math.atan2(z,x))/ math.pi)
        angle = angle + degrees
        rad = -angle * math.pi / 180
        return Position(math.cos(rad), math.sin(rad))

    def myclone(self):
        return Position(self.x, self.y, self.z)

    def toString(self):
        return str("("+ self.x + "," + self.z + ")")