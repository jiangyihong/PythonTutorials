from matplotlib import pyplot as plt
from die import Die

# 模拟投掷两个骰子
die1 = Die()
die2 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll() * die2.roll()
    results.append(result)

# 分析结果
max_result = die1.num_sides ** 2
frequencies = []
numbers = [m * n for m in range(1, die1.num_sides + 1)
           for n in range(1, die2.num_sides + 1)]
numbers = sorted(set(numbers))
for value in numbers:
    frequency = results.count(value)
    frequencies.append(frequency)

# 数据可视化
plt.title("Result of rolling two D6 1000 times")
plt.xlabel("Result")
plt.ylabel("Frequency of Result")
plt.scatter(numbers, frequencies)
plt.show()

