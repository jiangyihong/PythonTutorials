import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = "sitka_weather_2014.csv"
with open(filename) as file_object:
    reader = csv.reader(file_object)
    headers_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

# 数据可视化
fig = plt.figure(dpi=128, figsize=(10, 5))
plt.plot(dates, highs, c="red")
plt.plot(dates, lows, c="blue")
plt.title("Daily high and low temperatures - 2014")
plt.xlabel("", fontsize=24)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis="both", which="major", labelsize=16)
plt.show()
