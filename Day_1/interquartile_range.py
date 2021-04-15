"""
Author: Charles Herrmann
Date: 4/14/21
Objective: In this challenge, we practice calculating the interquartile range.
Task: The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e., Q3-Q1). Given an array, values, of n integers and an array, freqs, representing the respective frequencies of values's elements, construct a data set, S, where each values[i] occurs at frequency freqs[i]. Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place (i.e., 12.3 format).
Input Format: The first line contains an integer, n, the number of elements in arrays values and freqs. The second line contains n space-separated integers describing the elements of array values. The third line contains n space-separated integers describing the elements of array freqs.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#


def interQuartile(values, freqs):
    # create local variables
    S = []

    # fill S with values
    for i in range(len(values)):
        for j in range(freqs[i]):
            S.append(values[i])

    # sort the new array
    S.sort()

    # calculate middle index and upper/lower arrays
    if len(S) % 2 == 0:
        middleIdx = int(len(S) / 2)
        lower = S[:middleIdx]
        upper = S[middleIdx:]
    else:
        middleIdx = int(len(S) / 2) + 1
        lower = S[: middleIdx - 1]
        upper = S[middleIdx:]

    # calculate half index
    halfIdx = int(len(lower) / 2)

    # calculate Q1
    if len(lower) % 2 == 0:
        q1 = float((lower[halfIdx - 1] + lower[halfIdx]) / 2)
    else:
        q1 = float(lower[halfIdx])

    # calculate Q3
    if len(upper) % 2 == 0:
        q3 = float((upper[halfIdx - 1] + upper[halfIdx]) / 2)
    else:
        q3 = float(upper[halfIdx])

    print(q3 - q1)


if __name__ == "__main__":
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
