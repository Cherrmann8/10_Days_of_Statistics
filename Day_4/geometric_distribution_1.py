"""
Author: Charles Herrmann

Date: 4/17/21

Objective: In this challenge, we learn about geometric distributions.

Task: The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect occurs the 5th item produced?

Input Format: The first line contains the respective space-separated numerator and denominator for the probability of a defect, and the second line contains the inspection we want the probability of being the first defect for: 1 3, 5. If you do not wish to read this information from stdin, you can hard-code it into your program.
"""

import math
import os
import random
import re
import sys

# Enter your code here. Print output to STDOUT


def geometric(n, p):
    return math.pow((1 - p), (n - 1)) * p


if __name__ == "__main__":
    p = 1 / 3
    n = 5

    result = geometric(n, p)

    print(round(result, 3))
