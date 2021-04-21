"""
Author: Charles Herrmann

Date: 4/18/21

Objective: In this challenge, we learn about Poisson distributions.

Task: A random variable, X, follows Poisson distribution with mean of 2.5. Find the probability with which the random variable X is equal to 5.

Input Format: The first line contains X's mean. The second line contains the value we want the probability for: 2.5, 5. If you do not wish to read this information from stdin, you can hard-code it into your program.
"""

# Enter your code here. Print output to STDOUT

import math

if __name__ == "__main__":
    poisson = lambda k, m: (math.pow(m, k) * math.pow(math.e, -m)) / (math.factorial(k))

    print("{:.3f}".format(poisson(5, 2.5)))