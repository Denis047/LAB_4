import math

g = 9.81


class ProjectileMotion:
    class FreeMovement:
        def __init__(self, h):
            self.h = h
            self.g = g
            self.t = math.sqrt((2 * h) / self.g)

        def speed(self):
            speed = self.g * self.t
            return speed

    class LimitedMovement:

        def __init__(self, h, v2):
            self.h = h
            self.v2 = v2
            self.k = 0.01
            self.m = 7
            self.a = ((self.m * g - self.k * (v2 ** 2)) / self.m)
            self.t = math.sqrt((2 * h) / self.a)

        def speed(self):
            speed = self.a * self.t
            return speed



