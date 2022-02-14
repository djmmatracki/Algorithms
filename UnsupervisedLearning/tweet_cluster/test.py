import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0, 2*np.pi, 1000)

x = np.array([np.sin(t), np.cos(t)])
print(x)
# l2 = lambda x: np.sqrt(np.sum(x)**2)
# plt.plot(t, l2(x))
# plt.show()