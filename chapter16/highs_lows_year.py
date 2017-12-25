import csv
from matplotlib import pyplot as plt
from datetime import datetime


# 读取CSV文件
filename = "sitka_weather_2014.csv"
with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

# 数据可视化
fig = plt.figure(dpi=128, figsize=(10, 5))
plt.plot(dates, highs, c="red")
plt.title("Daily high temperatures - 2014", fontsize=24)
plt.xlabel("", fontsize=24)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)", fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()

