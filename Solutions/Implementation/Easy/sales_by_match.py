#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    # Count the total number of socks of each colour
    number_count = {}
    for i in range(n):
        number_count[ar[i]] = 0
    for i in range(n):
        number_count[ar[i]] += 1
    # Count the number of pairs
    pair_count = 0
    colours = list(number_count.keys())
    for i in range(len(number_count)):
        pair_count += int(number_count[colours[i]] / 2)
    print(pair_count)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
    
    # fptr.write(str(result) + '\n')

    # fptr.close()
