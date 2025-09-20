import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("./lab4/t4.txt", skiprows=1)

x = data[:, 0]
y = data[:, 1:]

ux = np.unique(x)

ay = []

for val in ux:
    ind = np.where(x == val)

    avg = np.mean(y[ind], axis=0)

    ay.append(avg)

ay = np.array(ay)

for a in range(ay.shape[0]):
    plt.plot(ux, ay[:, a], marker="o", label=f"Y{a + 1}")

plt.title("График средних значений")
plt.xlabel("X")
plt.ylabel("Ср. Y")
plt.grid()
plt.legend()

plt.show()
