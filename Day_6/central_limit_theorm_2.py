"""
Author: Charles Herrmann

Date: 4/19/21

Objective: In this challenge, we practice solving problems based on the Central Limit Theorem.

Task: The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of μ = 2.4 and a standard deviation of σ = 2.0. A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?

Input Format: There are 4 lines of input (shown below):
 - 250
 - 100
 - 2.4
 - 2.0
The first line contains the number of last-minute tickets available at the box office. The second line contains the number of students waiting to buy tickets. The third line contains the mean number of purchased tickets, and the fourth line contains the standard deviation. If you do not wish to read this information from stdin, you can hard-code it into your program.
"""

# Enter your code here. Print output to STDOUT

import math

if __name__ == "__main__":
    x, n, mean, std = 250, 100, 2.4, 2.0

    mean_sum = mean * n
    std_sum = math.sqrt(n) * std

    cdf = lambda x, u, o: 0.5 * (1 + math.erf((x - u) / (o * math.sqrt(2))))

    print(f"{cdf(x, mean_sum, std_sum):.4f}")
