from random import choice


class RandomWalk(object):
    """一个生成随机漫步数组的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有点的起始位置都是(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            # 设置x方向坐标值
            x_direction = choice([-1, 1])
            x_distance = choice([1, 2, 3, 4])
            x_step = x_direction * x_distance

            # 设置y方向坐标值
            y_direction = choice([-1, 1])
            y_distance = choice([1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 计算下一步的坐标
            x_next = self.x_values[-1] + x_step
            y_next = self.y_values[-1] + y_step

            # 拒绝原地踏步
            if x_next == 0 and y_next == 0:
                continue

            self.x_values.append(x_next)
            self.y_values.append(y_next)
