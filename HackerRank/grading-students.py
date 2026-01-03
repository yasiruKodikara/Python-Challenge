#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    rounded_grades = []
    for i in grades:
        if i < 38:
            grade = i
        else:
            rounded_grade = 5 * round((i / 5) + 0.5)
            diff = rounded_grade - i
            if diff < 3:
                grade = rounded_grade
            else:
                grade = i

        rounded_grades.append(grade)
    return rounded_grades


if __name__ == '__main__':


    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print('\n'.join(map(str, result)))

