# Naive batch GD
# Cost / Target function: y = (x + 5)^2
# starting point : x = 3

def calculate_gradient(x):
    return 2 * (x + 5)

cur_x = 3   #Algorithm start at x = 3
learning_rate = 0.01
max_iteration = 500

for i in range(max_iteration):
    cur_x = cur_x - learning_rate * calculate_gradient(cur_x)
    if ( (i+1) % 100 == 0):
        print('x value: ', cur_x)
