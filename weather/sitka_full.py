

import csv
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime

sitka_full = Path(r'weather\weather_data\sitka_weather_2021_full.csv')
dv_full = Path(r'weather/weather_data/death_valley_2021_simple.csv')

lines = sitka_full.read_text(encoding='utf-8').splitlines()
dv_lines = dv_full.read_text(encoding='utf-8').splitlines()



csv_obj = csv.reader(lines)
dv_csv_obj = csv.reader(dv_lines)

next(dv_csv_obj)
header = next(csv_obj)



rainfalls = []
dates = []
rainfalls_dv = []
dv_temps = []
sk_temps = []

for v, dv in zip(csv_obj, dv_csv_obj):
    try:
        sk_t = float(v[7])
        dv_t = float(dv[3])
        date = v[2]
        rainfall = float(v[5])
        rainfall_dv = float(dv[5])
        
        
    
    except ValueError as e:
        print(str(e))
        
    else:

        dates.append(datetime.strptime(date, r'%Y-%m-%d'))
        rainfalls.append(round(rainfall, 2))
        rainfalls_dv.append(round(rainfall_dv, 2))
        dv_temps.append(float(dv_t))
        sk_temps.append(float(sk_t))

print(rainfalls_dv)

fig, ax = plt.subplots()
ax.scatter(dv_temps, sk_temps)
# ax.plot(dates, rainfalls, color='blue')
# ax.plot(dates, rainfalls_dv, color='red')





# ax.fill_between(dates, rainfalls, rainfalls_dv, facecolor='green', alpha=0.2)
# fig.autofmt_xdate()
plt.show()