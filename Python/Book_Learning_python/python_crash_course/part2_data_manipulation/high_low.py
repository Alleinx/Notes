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
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[-1])
        except ValueError:
            print('missing data.')
        except Exception:
            print('Error occured.')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    plt.plot(dates, highs, c = 'red', label='high')
    plt.plot(dates, lows, c='blue', label='low')
    plt.fill_between(dates, highs, lows, facecolor='orange', alpha=0.3)
    plt.legend(loc = 'upper left')
    plt.show()
