from numpy import *
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("watermelon3.csv")
alt = array(df[['Idx', 'density', 'ratio_sugar', 'label']])
x0 = []
y0 = []
x1 = []
y1 = []
for a in alt:
    if a[3] == 1:
        x1.append(a[1])
        y1.append(a[2])
    elif a[3] == 0:
        x0.append(a[1])
        y0.append(a[1])
x0, x1, y0, y1 = array(x0), array(x1), array(y0), array(y1)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.figure()
plt.scatter(x0, y0, s=100, c='red', label='bad')
plt.scatter(x1, y1, s=100, c='green', label='good')
plt.xlabel("密度")
plt.ylabel("甜度")
plt.title("watermelon3α")
plt.show()
