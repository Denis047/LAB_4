import matplotlib.pyplot as plt


class Connected_Movement:

    def __init__(self, v0, h):
        self.v0 = v0
        self.h = h
        self.g = 9.8

    def time_of_flight(self):
        return 2 * self.v0 / self.g

    def height(self, t):
        return self.h - 0.5 * self.g * t ** 2

    def velocity(self, t):
        return self.v0 - self.g * t

    @staticmethod
    def plot_motion(connected_movement1, connected_movement2):
        t_max = max(connected_movement1.time_of_flight(), connected_movement2.time_of_flight())
        t_values = [0.01 * i for i in range(int(100 * t_max) + 1)]

        h1_values = [connected_movement1.height(t) for t in t_values]
        h2_values = [connected_movement2.height(t) for t in t_values]

        plt.plot(t_values, h1_values, label="Object 1")
        plt.plot(t_values, h2_values, label="Object 2")

        plt.xlabel('Час, с')
        plt.ylabel('Висота, м')
        plt.legend()
        plt.grid(True)
        plt.show()
