"""
Author: Charles Herrmann

Date: 4/21/21

Objective: In this challenge, we practice using linear regression techniques. 

Task: A group of five students enrolls in Statistics immediately after taking a Math aptitude test. Each student's Math aptitude test score, x, and Statistics course grade, y, can be expressed as the following list of (x, y) points:
1. (95, 85)
2. (85, 95)
3. (80, 70)
4. (70, 65)
5. (60, 70)
If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics? Determine the equation of the best-fit line using the least squares method, then compute and print the value of y when x = 80.

Input Format: There are five lines of input; each line contains two space-separated integers describing a student's respective x and y grades:
 - 95 85
 - 85 95
 - 80 70
 - 70 65
 - 60 70
If you do not wish to read this information from stdin, you can hard-code it into your program.
"""

# Enter your code here. Print output to STDOUT

from statistics import mean, pstdev


def pearson(x, y):
    n = len(x)
    mx, sx, my, sy = mean(x), pstdev(x), mean(y), pstdev(y)
    return sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / (n * sx * sy)


def linear_regression(x, y):
    b = pearson(x, y) * pstdev(y) / pstdev(x)
    return mean(y) - b * mean(x), b


if __name__ == "__main__":
    x = [95, 85, 80, 70, 60]
    y = [85, 95, 70, 65, 70]

    a, b = linear_regression(x, y)

    # to make prediction
    x_test = 80
    y_test = a + b * x_test
    print(f"{y_test:.3f}")
