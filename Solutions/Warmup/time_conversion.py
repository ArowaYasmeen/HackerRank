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
    form = s[-2] + s[-1] # Checking whether AM or PM
    if form == 'AM':
        hour, minute, second = s.split(":") # splitting the times
        if hour == '12' and int(minute) == 0:
            hour = '00'
            new_time = hour + ":" + minute + ":" + second[:-2]
            return new_time
        elif hour == '12' and int(minute) > 0:
            hour = '00'
            new_time = hour + ":" + minute + ":" + second[:-2]
            return new_time
        else:
            return s[:-2]
    else:
        hour, minute, second = s.split(":") # splitting the times
        if hour == '12' and int(minute) == 0:
            hour = '12'
            new_time = hour + ":" + minute + ":" + second[:-2]
            return new_time
        elif hour == '12' and int(minute) > 0:
            hour = '12'
            new_time = hour + ":" + minute + ":" + second[:-2]
            return new_time
        else:
            new_time = str(int(hour) + 12) + ':' + minute + ':' + second[:-2]

    return new_time

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)
    print(result)
