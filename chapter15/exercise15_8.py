from die import Die
import pygal


# 创建两个8点的骰子
die1 = Die(8)
die2 = Die(8)

# 投掷1000次并记录结果
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

# 分析统计结果
max_result = die1.num_sides + die2.num_sides
frequencies = []
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 可视化数据
hist = pygal.Bar()
hist.title = "Result of roll two D8 dice 1000 times"
hist.x_labels = [str(number) for number in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D8 + D8", frequencies)
hist.render_to_file("d8_dice_visual.svg")
