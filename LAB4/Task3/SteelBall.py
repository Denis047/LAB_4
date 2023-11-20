import math


class SteelBall:
    def __init__(self):
        self.g = 9.81
        self.v0 = 10

    def max_distance(self, alph):
        l_2 = []
        for alpha in range(alph):
            m = ((self.v0 ** 2) * math.sin(2 * alpha * math.pi / 180)) / self.g
            l_2.append(m)
        return l_2

    @staticmethod
    def angle(alph=90):
        alpha_2 = []
        for alpha in range(alph):
            alpha_2.append(alpha)
        return alpha_2
