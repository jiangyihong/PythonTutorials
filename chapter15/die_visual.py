from chapter15.die import Die
import pygal

die = Die()

results = []

for roll_num in range(1000):
    results.append(die.roll())

frequencies = []
for value in range(1, die.num_sides + 1):
    frequencies.append(results.count(value))

hist = pygal.Bar()

hist.title = "Results of rolling one D6 in 1000 times."
hist.x_labels = [str(number) for number in range(1, 7)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6", frequencies)
hist.render_to_file("die_visual.svg")
