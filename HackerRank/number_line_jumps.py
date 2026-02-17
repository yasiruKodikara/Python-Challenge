#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    tot_1 = x1
    tot_2 = x2

    while 1:
        if tot_1 == tot_2:
            return 'YES'
        if tot_1 >= 10000 or tot_2 >= 10000 or tot_1 >= tot_2:
            return 'NO'
            break
        tot_1 += v1
        tot_2 += v2


if __name__ == '__main__':


    first_multiple_input = [1571,4240,9023,4234]

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)
