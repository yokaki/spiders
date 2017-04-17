import matplotlib.pylab as plt
from random import randint

x = [randint(0, 20) for _ in range(10)]
y = [randint(1000, 2000) for _ in range(10)]
plt.plot(x, y)
plt.show()
