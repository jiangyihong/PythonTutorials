import matplotlib.pyplot as plt


plt.title("Cube Numbers")
plt.xlabel("Value")
plt.ylabel("Cube of Value")
x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]
plt.scatter(x_values, y_values)
plt.show()
