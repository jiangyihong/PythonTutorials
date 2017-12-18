from matplotlib import pyplot as plt


plt.title("Cube Numbers")
plt.xlabel("Value")
plt.ylabel("Cube of Values")
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues)
plt.show()
