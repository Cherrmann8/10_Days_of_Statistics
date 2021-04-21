"""
Author: Charles Herrmann

Date: 4/19/21

Objective: In this challenge, we practice solving problems based on the Central Limit Theorem.

Task: A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of μ = 205 pounds and a standard deviation of σ = 15 pounds. Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?

Input Format: There are 4 lines of input (shown below):
 - 9800
 - 49
 - 205
 - 15
The first line contains the maximum weight the elevator can transport. The second line contains the number of boxes in the cargo. The third line contains the mean weight of a cargo box, and the fourth line contains its standard deviation. If you do not wish to read this information from stdin, you can hard-code it into your program.
"""

# Enter your code here. Print output to STDOUT

import math

if __name__ == "__main__":
    x, n, mean, std = 9800, 49, 205, 15

    mean_sum = mean * n
    std_sum = math.sqrt(n) * std

    cdf = lambda x, u, o: 0.5 * (1 + math.erf((x - u) / (o * math.sqrt(2))))

    print(f"{cdf(x, mean_sum, std_sum):.4f}")
