import matplotlib.pyplot as plt
import numpy as np


class KinematicMotion:
    def __init__(self, v0, k2):
        self.v0 = v0
        self.k2 = k2

    def time_of_flight_without_drag(self):
        g = 9.81
        return (2 * self.v0) / g

    def time_of_flight_with_drag(self):
        g = 9.81
        t = 0
        v = self.v0
        dt = 0.01
        while v > 0:
            v -= (self.k2 * v * abs(v) * dt)
            v -= g * dt
            t += dt
        return t

    def plot_motion(self):
        t_without_drag = self.time_of_flight_without_drag()
        t_with_drag = self.time_of_flight_with_drag()

        t = np.linspace(0, max(t_without_drag, t_with_drag), 100)
        v_without_drag = -9.81 * t + self.v0
        v_with_drag = np.zeros_like(t)
        for i in range(len(t)):
            if v_with_drag[i - 1] > 0:
                v_with_drag[i] = v_with_drag[i - 1] - (self.k2 * v_with_drag[i - 1] * abs(v_with_drag[i - 1]) + 9.81)
            else:
                v_with_drag[i] = 0

        plt.plot(t, v_without_drag, label='Без гальмівної сили')
        plt.plot(t, v_with_drag, label='З гальмівною силою')
        plt.xlabel('Час (с)')
        plt.ylabel('Швидкість (м/с)')
        plt.legend()
        plt.title('Графіки руху тіла')
        plt.grid()
        plt.show()
