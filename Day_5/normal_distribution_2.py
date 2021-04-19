"""
Author: Charles Herrmann

Date: 4/18/21

Objective: In this challenge, we go further with normal distributions.

Task: The final grades for a Physics exam taken by a large group of students have a mean of μ = 70 and a standard deviation of σ = 10. If we can approximate the distribution of these grades by a normal distribution, what percentage of the students: Scored higher than 80 (i.e., have a grade > 80)? Passed the test (i.e., have a grade >= 60)? Failed the test (i.e., have a grade < 60)? Find and print the answer to each question on a new line, rounded to a scale of 2 decimal places.

Input Format: There are 3 lines of input (shown below):
 - 70 10
 - 80
 - 60
The first line contains 2 space-separated values denoting the respective mean and standard deviation for the exam. The second line contains the number associated with question 1. The third line contains the pass/fail threshold number associated with questions 2 and 3. If you do not wish to read this information from stdin, you can hard-code it into your program.
"""

# Enter your code here. Print output to STDOUT

import math

if __name__ == "__main__":
    mean, std = 70, 10
    cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

    # Greater than 80
    print("{:.2f}".format(cdf(60) * 100))
    # Greater than or equal to 60
    print("{:.2f}".format(cdf(80) * 100))
    # Less than 60
    print("{:.2f}".format(cdf(60) * 100))
