#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    points_a = 0
    points_b = 0
    tot = []

    for i in range(3):
        if (a[i] > b[i]):
            points_a += 1
        elif (a[i] < b[i]):
            points_b += 1
        else:
            pass
    tot.append(points_a)
    tot.append(points_b)
    return tot


if __name__ == '__main__':


    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print((' '.join(map(str, result))))



