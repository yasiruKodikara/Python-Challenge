#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    M = s[-2:]


    if (M == "AM"):

        HH = int(s[0:2])

        if (HH == 12):
            HH24 = "00" + s[2:-2]
            return HH24
        else:

            return HH


    elif(M == "PM"):
        if(s[0:2] == "12"):
            return s[0:-2]
        else:
            hh12 = int(s[0:2])
            hh24 = hh12 + 12
            hh24 = str(hh24)
            s = hh24 + s[2:-2]

            return s


if __name__ == '__main__':


    s = input()

    result = timeConversion(s)

    print(result)
