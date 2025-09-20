import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

t = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = t**2
x = t**2 * np.sin(t)
y = t**2 * np.cos(t)

ax.plot(x, y, z, label="parametric curve")
ax.legend()

plt.show()
