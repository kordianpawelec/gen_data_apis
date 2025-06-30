from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# path = Path(r'weather\weather_data\sitka_weather_07_2021_simple.csv')
path = Path(r'weather\weather_data\sitka_weather_2021_simple.csv')

lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)

header_row = next(reader)

highs = []
lows = []
dates = []
# print(reader[2][4])
for row in reader:
    high = int(row[4])
    low = int(row[5])
    date = datetime.strptime(row[2], r'%Y-%m-%d')
    dates.append(date)
    highs.append(high)
    lows.append(low)
print(highs)

vals = range(1, len(highs) + 1)

plt.style.use('classic')

fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='green', alpha=0.5)
ax.fill_between(dates, lows, highs, facecolor='green', alpha=0.1)
ax.set_title('high sitka temp')
ax.set_xlabel('dates')
fig.autofmt_xdate()
ax.set_ylabel('temp highs')
ax.tick_params(labelsize=10)

plt.show()