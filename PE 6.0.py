#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum_of_squares = (n*(n+1)*(2*n+1))/6
    square_of_sum = ((n*(n+1))/2)**2
    difference = int(square_of_sum - sum_of_squares)
    print(difference)