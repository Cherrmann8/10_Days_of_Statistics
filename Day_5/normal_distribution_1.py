"""
Author: Charles Herrmann
Date: 4/18/21
Objective: In this challenge, we learn about normal distributions. 
Task: In a certain plant, the time taken to assemble a car is a random variable, X, having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. What is the probability that a car can be assembled at this plant in: Less than 19.5 hours? Between 20 and 22 hours?
Input Format: There are 3 lines of input (shown below):
 - 20 2
 - 19.5
 - 20 22
The first line contains 2 space-separated values denoting the respective mean and standard deviation for X. The second line contains the number associated with question 1. The third line contains 2 space-separated values describing the respective lower and upper range boundaries for question 2. If you do not wish to read this information from stdin, you can hard-code it into your program.
"""

# Enter your code here. Print output to STDOUT

import math

if __name__ == "__main__":
    mean, std = 20, 2

    cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

    # Less than 19.5
    print("{:.3f}".format(cdf(19.5)))
    # Between 20 and 22
    print("{:.3f}".format(cdf(22) - cdf(20)))
