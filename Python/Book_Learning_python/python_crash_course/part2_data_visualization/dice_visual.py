# pygal play
import pygal

from dice import Dice

dice = Dice()

results = []
for roll_num in range(1000):
    result = dice.roll()
    results.append(result)

frequencies = []
# Analyze result
for value in range(1, dice.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist._title = 'Results of rolling one D6 1000 times.'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist._x_title = 'Result'
hist._y_title = 'Frequence of Result'

hist.add('D6', frequencies)

hist.render_to_file('dice_visual.svg')
