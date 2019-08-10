# pygal play
import pygal

from dice import Dice

dice1 = Dice()
dice2 = Dice(10)

results = [dice1.roll() * dice2.roll() for _ in range(10000)]

iter_num = (dice1.num_sides*dice2.num_sides) + 1

# Analyze result
frequencies = [results.count(value) for value in range(1, iter_num)]

hist = pygal.Bar()

hist._title = 'Results of rolling D6 * D10 10,000 times.'
hist._x_title = 'Result'
hist._y_title = 'Frequence of Result'

hist.x_labels = [str(i) for i in range(1, iter_num)]
# pass value to the graph
hist.add('D6  D10', frequencies)

hist.render_to_file('dice_visual.svg')
