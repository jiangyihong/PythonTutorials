from chapter15.die import Die
import pygal

die1 = Die()
die2 = Die()

results = []
for roll_num in range(1000):
    results.append(die1.roll() + die2.roll())

frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
    frequencies.append(results.count(value))

# 可视化结果
hist = pygal.Bar()
hist.title = "Result of rolling two D6 dice 1000 times"
hist.x_labels = [str(number) for number in range(2, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add("D6 + D6", frequencies)
hist.render_to_file("dice_visual.svg")

