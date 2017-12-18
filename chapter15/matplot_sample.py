from matplotlib import pyplot as plt


x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.title("Square Numbers")
plt.xlabel("Value")
plt.ylabel("Square of Values")
plt.scatter(x_values, y_values)
plt.show()
