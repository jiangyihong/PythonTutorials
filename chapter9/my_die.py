from chapter9.die import Die


six_die = Die()
for i in range(0, 10):
    six_die.roll_die()
print("\n")

ten_die = Die(10)
for j in range(0, 10):
    ten_die.roll_die()
print("\n")

twenty_die = Die(20)
for k in range(0, 10):
    twenty_die.roll_die()
