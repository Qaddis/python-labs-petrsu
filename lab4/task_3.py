import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-4, 4, 400)
f = 1 / (1 + t * 1j)

re = np.real(f)
im = np.imag(f)

module = np.abs(f)

plt.scatter(re, im, c=module, cmap="viridis", alpha=0.7)

plt.title("f(t) = 1 / (1 + it)")
plt.xlabel("Re(f)")
plt.ylabel("Im(f)")
plt.grid()

plt.show()
