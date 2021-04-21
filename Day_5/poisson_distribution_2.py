"""
Author: Charles Herrmann

Date: 4/18/21

Objective: In this challenge, we go further with Poisson distributions.

Task: The manager of a industrial plant is planning to buy a machine of either type A or type B. For each day’s operation:
 - The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88. The daily cost of operating A is C_A = 160 + 40 * X ** 2.
 - The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55. The daily cost of operating B is C_B = 128 + 40 * Y ** 2.
Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.

Input Format: A single line comprised of 2 space-separated values denoting the respective means for A and B: 0.88 1.55. If you do not wish to read this information from stdin, you can hard-code it into your program.
"""

# Enter your code here. Print output to STDOUT

import math

if __name__ == "__main__":
    ma = 0.88
    mb = 1.55

    ea = ma + math.pow(ma, 2)
    eb = mb + math.pow(mb, 2)

    ca = 160 + (40 * ea)
    cb = 128 + (40 * eb)

    print(round(ca, 3))
    print(round(cb, 2))
