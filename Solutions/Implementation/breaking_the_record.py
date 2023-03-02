#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min_count = 0
    max_count = 0

    for i, score in ernumerate(scores):
        if i == 0:
            min_score = score
            max_score = score
            min_count = 0
            max_count = 0
        else:
            if score < min_score:
                min_score = score
                min_count += 1
            elif score > max_score:
                max_score = score
                max_count += 1
    return max_count, min_count, 

if __name__ == '__main__':

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)
