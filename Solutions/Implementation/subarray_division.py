#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    sliding_window_size = m
    possible_breaks = []

    for i in range(len(s) - sliding_window_size + 1):
        sum = 0
        for j in range(i, i + sliding_window_size):
            sum += s[j]
        if sum == d:
            possible_breaks.append([i, i + sliding_window_size - 1])

    return len(possible_breaks)

if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

