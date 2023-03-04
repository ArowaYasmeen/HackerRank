#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    # List of sightings of birds identified by index
    # e.g. count_of_sighting[2] = 3 means that bird 2 was sighted thrice
    count_of_sightings = {}
    # Initialise the list
    for i in range(len(arr)):
        count_of_sightings[arr[i]] = 0
    for i in range(len(arr)):
        count_of_sightings[arr[i]] += 1

    # List of keys and values 
    sighting_counts = list(count_of_sightings.values())
    bird_numbers = list(count_of_sightings.keys())
    
    # Maximum sighting count
    max_count = max(sighting_counts)
    
    # Bird numbers with the maximum sighting count
    bird_numbers_with_max_sighting = []
    for i in range(len(sighting_counts)):
        if sighting_counts[i] == max_count:
            bird_numbers_with_max_sighting.append(bird_numbers[i])
    
    smallest_ID_with_max_sighting = min(bird_numbers_with_max_sighting)


    return smallest_ID_with_max_sighting

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
