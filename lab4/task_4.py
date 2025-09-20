import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("./lab4/t4.txt", skiprows=1)

x = data[:, 0]
y = data[:, 1:]

means = np.mean(y, axis=1)
errors = np.std(y, axis=1)

ux = np.unique(x)

mean_vals = []
errors_vals = []

for val in ux:
    rows = np.where(x == val)

    mean_vals.append(np.mean(y[rows]))
    errors_vals.append(np.std(y[rows]))

mean_vals = np.array(mean_vals)
errors_vals = np.array(errors_vals)

plt.errorbar(
    ux,
    mean_vals,
    yerr=errors_vals,
    fmt="o-y",
    capsize=5,
    elinewidth=2,
    ecolor="r",
    label="Измеренные данные",
)

plt.title("График средних значений с отклонениями")
plt.xlabel("X")
plt.ylabel("Средние значения")
plt.legend()
plt.grid()

plt.show()
