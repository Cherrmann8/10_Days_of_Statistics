"""
Author: Charles Herrmann
Date: 4/14/21
Objective: In this challenge, we practice calculating quartiles.
Task: Given an array, arr, of n integers, calculate the respective first quartile (Q1), second quartile (Q2), and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def quartiles(arr):
    # create local variable and sort input
    qs = [0, 0, 0]
    arr.sort()

    # calculate middle index and upper/lower arrays
    if len(arr) % 2 == 0:
        middleIdx = int(len(arr) / 2)
        lowerHalf = arr[:middleIdx]
        upperHalf = arr[middleIdx:]
    else:
        middleIdx = int(len(arr) / 2) + 1
        lowerHalf = arr[: middleIdx - 1]
        upperHalf = arr[middleIdx:]

    # calculate half index for upper/lower arrays
    halfIdx = int(len(lowerHalf) / 2)

    # calculate Q2
    if len(arr) % 2 == 0:
        qs[1] = int((arr[middleIdx - 1] + arr[middleIdx]) / 2)
    else:
        qs[1] = arr[middleIdx - 1]

    # calculate Q1
    if len(lowerHalf) % 2 == 0:
        qs[0] = int((lowerHalf[halfIdx - 1] + lowerHalf[halfIdx]) / 2)
    else:
        qs[0] = lowerHalf[halfIdx]

    # calculate Q3
    if len(upperHalf) % 2 == 0:
        qs[2] = int((upperHalf[halfIdx - 1] + upperHalf[halfIdx]) / 2)
    else:
        qs[2] = upperHalf[halfIdx]

    return qs


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write("\n".join(map(str, res)))
    fptr.write("\n")

    fptr.close()