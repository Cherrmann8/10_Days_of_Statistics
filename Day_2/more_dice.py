"""
Author: Charles Herrmann
Date: 4/15/21
Objective: In this challenge, we practice calculating probability.
Task: In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that the values rolled by each die will be different and the two dice have a sum of 6.
"""


def calculateProbability(S, A):
    print(len(A) / len(S))


if __name__ == "__main__":
    S = [[i, j] for i in range(1, 7) for j in range(1, 7)]
    A = []
    for i in range(1, 7):
        for j in range(1, 7):
            if i != j and i + j == 6:
                A.append([i, j])
    calculateProbability(S, A)