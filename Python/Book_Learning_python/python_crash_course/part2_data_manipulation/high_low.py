import csv
from matplotlib import pyplot as plt
from datetime import datetime

file = 'data/sitka_weather_2018_simple.csv'
plt.figure(figsize=(15, 10))
plt.title('Daily high/low temperature of sitka in 2018')

with open(file) as f:
    csv_reader = csv.reader(f)
    
    # get header
    csv_header = next(csv_reader)
    # for index, item in enumerate(csv_header):
    #    print(index, item)

    dates, highs, lows = [], [], []
    for row in csv_reader:
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
        highs.append(int(row[5]))
        lows.append(int(row[-1]))

    plt.plot(dates, highs, c = 'red', label='high')
    plt.plot(dates, lows, c='blue', label='low')
    plt.legend(loc = 'upper left')
    plt.show()
