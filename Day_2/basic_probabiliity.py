"""
Author: Charles Herrmann

Date: 4/15/21

Objective: In this challenge, we practice calculating probability.

Task: In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most 9.
"""


def calculateProbability(S, A):
    print(len(A) / len(S))


if __name__ == "__main__":
    S = [[i, j] for i in range(1, 7) for j in range(1, 7)]
    A = []
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j <= 9:
                A.append([i, j])
    calculateProbability(S, A)