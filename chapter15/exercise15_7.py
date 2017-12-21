from die import Die
import pygal


# 创建三个D6的骰子
die1 = Die()
die2 = Die()
die3 = Die()

# 模拟投掷数据
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll() + die3.roll()
    results.append(result)

# 分析投掷结果
max_result = die1.num_sides * 3
frequencies = []
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 数据可视化
hist = pygal.Bar()
hist.title = "Results of rolling three D6 1000 times"
hist.x_labels = [str(number) for number in range(3, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file("d6_third_visual.svg")
