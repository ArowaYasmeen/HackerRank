#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    flip_from_front = math.floor(p / 2)
    if n%2 != 0:
        flip_from_back = math.floor((n - p) / 2)
    else:
        flip_from_back = math.ceil((n - p) / 2)

    return min(flip_from_front, flip_from_back)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
