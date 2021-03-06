import matplotlib.pyplot as plt

plt.title("Square Numbers", fontsize=24)
plt.xlabel("x value", fontsize=14)
plt.ylabel("y value", fontsize=14)

x = [i for i in range(1, 1001)]
y = [i**2 for i in x]

# ----------------------------
# Color & size
# plt.scatter(x, y, s=1, c = (0,0.7,0.7),edgecolors=None)
# s: size of a point.
# c: RGB color, should use a 2-D array with a single row if you
#       really want to specify the same RGB/RGBA value for all points.
#       the value should land between 0 ~ 1.

# ----------------------------
# edge color & color mapping
# c=y: change the color with the value of y.
# cmap: tell python which color to use for color mapping.
#   matplotlib.org -> examples -> color examples -> colormaps_reference for more color.
# edgecolors = 'none': remove the edge color of a point.
plt.scatter(x, y, c=y, cmap=plt.cm.Blues, edgecolors='none', s = 3)


# define the range of each axis.
plt.axis([0, 1100, 0, 1100000])

plt.show()
# ----------------------------
# Save Img:
# need to replace plt.show() with plt.savefig(), otherwise will give empty img.

# plt.savefig('squaares_plot.png', bbox_inches='tight')

# bbox_inches: remove empty space on the img, if want to reserve the empty space,
#   just ignore this parameter.
