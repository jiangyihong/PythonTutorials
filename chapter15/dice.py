from chapter15.die import Die
import pygal

die1 = Die()
die2 = Die()

results = []
for roll_number in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)


frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result):
    frequencies.append(results.count(value))

hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times"
hist.x_labels = [str(number) for number in range(2, max_result)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"


hist.add("D6 + D6 ", frequencies)
hist.render_to_file("dice_visual.svg")

