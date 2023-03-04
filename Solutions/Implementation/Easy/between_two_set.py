#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    a_set = set()
    b_set = set()

    #### Assuming that the input lists are in ascending order
    for i in range(1, b[-1] + 1):
        # Checking if i is a multiple of all elements in a
        if all([i % factor == 0 for factor in a]):
            a_set.add(i)
        # Checking if i is a factor of all elements in b
        if all([multiple % i == 0 for multiple in b]):
            b_set.add(i)
    
    return len(a_set.intersection(b_set)) # Returns the values in common

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)
