"""
Author: Charles Herrmann

Date: 4/19/21

Objective: In this challenge, we practice solving problems based on the Central Limit Theorem.

Task: You have a sample of 100 values from a population with mean μ = 500 and with standard deviation σ = 80. Compute the interval that covers the middle 95% of the distribution of the sample mean; in other words, compute A and B such that P(A < x < B) = 0.95. Use the value of z = 1.96. Note that z is the z-score.

Input Format: There are 5 lines of input (shown below):
 - 100
 - 500
 - 80
 - 0.95
 - 1.96
The first line contains the sample size. The second and third lines contain the respective mean (μ) and standard deviation (σ). The fourth line contains the distribution percentage we want to cover (as a decimal), and the fifth line contains the value of z. If you do not wish to read this information from stdin, you can hard-code it into your program.
"""

# Enter your code here. Print output to STDOUT

import math

if __name__ == "__main__":
    n, mean, std, interval, z = 100, 500, 80, 0.95, 1.96

    print(f"{mean - (std / math.sqrt(n)) * z:.2f}")
    print(f"{mean + (std / math.sqrt(n)) * z:.2f}")
