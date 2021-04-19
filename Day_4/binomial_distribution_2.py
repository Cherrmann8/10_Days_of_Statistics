"""
Author: Charles Herrmann
Date: 4/17/21
Objective: In this challenge, we go further with binomial distributions.
Task: A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain: 1) No more than 2 rejects and 2) At least 2 rejects?
Input Format: A single line containing the following values (denoting the respective percentage of defective pistons and the size of the current batch of pistons): 12 10. If you do not wish to read this information from stdin, you can hard-code it into your program.
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
    p = 0.12
    n = 10

    result = 0
    for i in range(0, 3):
        result += binomial(i, n, p)

    print(round(result, 3))

    result = 0
    for i in range(2, 11):
        result += binomial(i, n, p)

    print(round(result, 3))
