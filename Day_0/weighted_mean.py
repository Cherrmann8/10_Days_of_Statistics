"""
Author: Charles Herrmann
Date: 4/13/21
Objective: In the previous challenge, we calculated a mean. In this challenge, we practice calculating a weighted mean.
Task: Given an array, X, of N integers and an array, W, representing the respective weights of X's elements, calculate and print the weighted mean of X's elements. Your answer should be rounded to a scale of 1 decimal place (i.e., 12.3 format).
"""

import math
import os
import random
import re
import sys

#
# Complete the 'weightedMean' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY X
#  2. INTEGER_ARRAY W
#


def weightedMean(X, W):
    M = []
    for i in range(len(X)):
        M.append(X[i] * W[i])

    print(round(sum(M) / sum(W), 1))


if __name__ == "__main__":
    n = int(input().strip())
    vals = list(map(int, input().rstrip().split()))
    weights = list(map(int, input().rstrip().split()))
    weightedMean(vals, weights)