"""
Author: Charles Herrmann
Date: 4/14/21
Objective: In this challenge, we practice calculating standard deviation.
Task: Given an array, arr, of n integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3 format). An error margin of +/- 0.1 will be tolerated for the standard deviation.
Input Format: The first line contains an integer, n, denoting the size of arr. The second line contains n space-separated integers that describe arr.
"""

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def stdDev(arr):
    # calculate the mean
    mean = sum(arr) / len(arr)

    # calculate the squared mean sum
    sms = 0
    for a in arr:
        sms += math.pow(a - mean, 2)

    # calculate standard deviation
    sd = math.sqrt(sms / len(arr))

    print(sd)


if __name__ == "__main__":
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
