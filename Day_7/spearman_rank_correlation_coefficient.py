"""
Author: Charles Herrmann

Date: 4/20/21

Objective: In this challenge, we practice calculating Spearman's rank correlation coefficient.

Task: Given two n-element data sets, X and Y, calculate the value of Spearman's rank correlation coefficient.

Input Format: The first line contains an integer, n, denoting the number of values in data sets X and Y.
The second line contains n space-separated real numbers (scaled to at most one decimal place) denoting data set X.
The third line contains n space-separated real numbers (scaled to at most one decimal place) denoting data set Y.
"""

# Enter your code here. Print output to STDOUT


def get_rank(X, n):
    x_rank = dict((x, i + 1) for i, x in enumerate(sorted(set(X))))
    return [x_rank[x] for x in X]


if __name__ == "__main__":
    n = int(input().strip())

    X = list(map(float, input().rstrip().split()))
    Y = list(map(float, input().rstrip().split()))

    rx = get_rank(X, n)
    ry = get_rank(Y, n)

    d = [(rx[i] - ry[i]) ** 2 for i in range(n)]
    rxy = 1 - (6 * sum(d)) / (n * (n * n - 1))

    print(f"{rxy:.3f}")