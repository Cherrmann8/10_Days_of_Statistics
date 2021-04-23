"""
Author: Charles Herrmann

Date: 4/20/21

Objective: In this challenge, we practice calculating the Pearson correlation coefficient.

Task: Given two n-element data sets, X and Y, calculate the value of the Pearson correlation coefficient.

Input Format: The first line contains an integer, n, denoting the size of data sets X and Y.
The second line contains n space-separated real numbers (scaled to at most one decimal place), defining data set X.
The third line contains n space-separated real numbers (scaled to at most one decimal place), defining data set Y.
"""

# Enter your code here. Print output to STDOUT

import math


def mean_stdDev(arr):
    # calculate the mean
    mean = sum(arr) / len(arr)

    # calculate the squared mean sum
    sms = 0
    for a in arr:
        sms += math.pow(a - mean, 2)

    # calculate standard deviation
    sd = math.sqrt(sms / len(arr))

    return mean, sd


if __name__ == "__main__":
    n = int(input().strip())

    X = list(map(float, input().rstrip().split()))
    Y = list(map(float, input().rstrip().split()))

    xMean, xStdDev = mean_stdDev(X)
    yMean, yStdDev = mean_stdDev(Y)

    covariance = sum([(X[i] - xMean) * (Y[i] - yMean) for i in range(n)])

    correlation_coefficient = covariance / (n * xStdDev * yStdDev)

    print(f"{correlation_coefficient:.3f}")