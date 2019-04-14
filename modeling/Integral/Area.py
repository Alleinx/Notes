#This program calculate the Area under a curve using "Finite sums"
# function : f(x) = x^2
# Domain : [0,1]

import math

def calculate_value(x):
    return pow(x, 2)

def main():
    slice_num = 8  #The more slice token, the more precise the result is.

    stride = 1 / slice_num
    lower_area = 0
    upper_area = 0
    i = 0.0

    while(i < 1):
        lower_area += calculate_value(i) * stride
        i += stride

    print('lower bound:', lower_area)
    i = 0.0

    while (i < 1):
        upper_area += calculate_value(i+stride) * stride
        i += stride

    print('upper bound:', upper_area)

main()