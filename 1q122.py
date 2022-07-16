#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    total = 0


    i = 1
    j = 1
    k = 1

    while 3*i < n:
        total = total + 3*i
        i = i+1

    while 5*j < n:
        total = total + 5*j
        j = j+1

    while 15*k < n:
        total = total - 15*k
        k = k+1
    print(total)
