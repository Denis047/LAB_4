from matplotlib import pyplot as plt

from SteelBall import SteelBall

ball = SteelBall()
plt.plot(ball.angle(), ball.max_distance(90), 'r', linewidth=3)
plt.xlabel('Кут, °')
plt.ylabel('Відстань, м')
plt.title('Визначення максимальної відстані кидання каменю')
plt.grid(True)
plt.text(8, 1, 'Максимальна відстань = 10.15 при куті 45 градусів')
plt.show()
