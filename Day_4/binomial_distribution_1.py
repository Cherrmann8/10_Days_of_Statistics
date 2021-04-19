"""
Author: Charles Herrmann
Date: 4/17/21
Objective: In this challenge, we learn about binomial distributions.
Task: The ratio of boys to girls for babies born in Russia is 1.09 : 1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys? Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).
Input Format: A single line containing the following values: 1.09 1. If you do not wish to read this information from stdin, you can hard-code it into your program.
"""

import math
import os
import random
import re
import sys

# Enter your code here. Print output to STDOUT


def binomial(x, n, p):
    return (
        (math.factorial(n) / (math.factorial(x) * math.factorial(n - x)))
        * math.pow(p, x)
        * math.pow((1 - p), (n - x))
    )


if __name__ == "__main__":
    ratio = [1.09, 1]
    pBoy = ratio[0] / sum(ratio)
    n = 6
    result = 0

    for i in range(3, 7):
        result += binomial(i, n, pBoy)

    print(round(result, 3))
