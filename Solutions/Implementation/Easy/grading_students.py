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


def gradingStudents(grades):
    # Write your code here
    rounded_grades = [] # List of rounded grades
    for i in range(len(grades)):
        if grades[i] < 38:
            # No rounding occurs
            rounded_grades.append(grades[i])
        else:
            remainder = grades[i] % 5
            difference = 5 - remainder
            if difference < 3 :
                rounded_grades.append(grades[i] + difference)
            else:
                rounded_grades.append(grades[i])

    return rounded_grades

if __name__ == '__main__':

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
