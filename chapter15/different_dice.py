from chapter15.die import Die
import pygal

die1 = Die()
die2 = Die(10)

# 投掷骰子多次，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)
# 分析结果
max_result = die1.num_sides + die2.num_sides
frequencies = []
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 数据可视化
hist = pygal.Bar()
hist.title = "Result of rolling a D6 and a D10 50,000 times"
hist.x_labels = [str(number) for number in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6 + D10", frequencies)
hist.render_to_file("different_dice.svg")
