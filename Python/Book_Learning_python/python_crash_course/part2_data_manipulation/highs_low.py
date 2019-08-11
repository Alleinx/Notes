import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'data/sitka_weather_07-2018_simple.csv'
plt.figure(figsize=(15, 6))
plt.title('Daily high temperatures.', fontsize='16')

with open(filename) as f:
    reader = csv.reader(f)
    
    header_row = next(reader)
    # or reader.__next__()
    dates, highs = [], []

    for row in reader:
        highs.append(row[5])
        dates.append(datetime.strptime(row[2], "%Y-%m-%d"))

plt.plot(dates, highs, c='blue')
plt.ylabel('Temperature(F)', fontsize=16)
plt.xlabel('', fontsize=16)

plt.show()