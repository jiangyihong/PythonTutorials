import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.title("Square Numbers", fontsize=14)
plt.plot(input_value, squares, linewidth=5)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square", fontsize=14)

plt.tick_params(axis="both", labelsize=14)
plt.show()
