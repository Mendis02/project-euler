#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())


    for x in range(1,10000000):
        l = []
        for i in range(1,n+1):
            re = x % i
            l.append(re)
        y=sum(l)

        if y==0:
            print(x)
            break


