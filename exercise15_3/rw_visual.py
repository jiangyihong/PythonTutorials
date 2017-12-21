from matplotlib import pyplot as plt
from exercise15_3.random_walk import RandomWalk


rw = RandomWalk()
rw.fill_walk()
# 绘制散点图
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
