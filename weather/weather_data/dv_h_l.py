from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import csv


path = Path(r'weather\weather_data\death_valley_2021_simple.csv')

lines = path.read_text(encoding='utf-8').splitlines()
csv_obj = csv.reader(lines)
header = next(csv_obj)
for index, head in enumerate(header):
    print(index, head)
    
dates = []
highs = []
lows = []

for row in csv_obj:
    try:
        high = int(row[3])
        low = int(row[4])
        date = datetime.strptime(row[2], '%Y-%m-%d')

    except ValueError:
        print(f'error in {date}')
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)
        
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
ax.set_label('dates vs temp')
ax.set_xlabel('dates')
ax.set_ylabel('temps')


fig.autofmt_xdate()

ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.tick_params(labelsize = 10)
plt.show()