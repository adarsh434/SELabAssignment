import matplotlib.pyplot as plt
import seaborn as sns

x = [2, 4, 6, 8, 10, 12, 14, 16, 18]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9]

plt.plot(x, markerfacecolor= '#CD0000', marker='o', markersize='10', markevery=50)
plt.plot(y, color="red", markeredgecolor="blue", markerfacecolor="yellow", marker="o", markersize=10, label="Cube")

plt.plot(x,y)

plt.title("Square and Cubes")
plt.xlabel("Initial values")
plt.ylabel("Computed values")
plt.grid(b=True, which="both", color="gray", alpha=0.6)
plt.legend()

plt.show()

sns.displot(y, kde=True, color="m")     # seaborn
plt.show()
