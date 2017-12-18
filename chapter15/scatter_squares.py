import matplotlib.pyplot as plt


plt.title("Square Numbers")
plt.xlabel("Value")
plt.ylabel("Square of Value")
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors="none")
plt.savefig("squares_plot.png", bbox_inches="tight")


