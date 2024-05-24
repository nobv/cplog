# https://www.hackerrank.com/challenges/truck-tour/problem
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#


def truckTour(petrolpumps):
    # Write your code here
    """
    解説
    - https://www.youtube.com/watch?v=8RZoDkt9i3c
    """
    start = petrol_in_truck = 0
    amount, distance = zip(*petrolpumps)

    for i in range(len(distance)):
        petrol_in_truck += amount[i] - distance[i]
        if petrol_in_truck < 0:
            start = i + 1
            petrol_in_truck = 0
    return start


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + "\n")

    fptr.close()
