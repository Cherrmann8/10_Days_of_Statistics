"""
Author: Charles Herrmann
Date: 4/15/21
Objective: In this challenge, we practice calculating the probability of a compound event.
Task: There are 3 urns labeled X, Y, and Z. Urn X contains 4 red balls and 3 black balls. Urn Y contains 5 red balls and 4 black balls. Urn Z contains 4 red balls and 4 black balls. One ball is drawn from each of the 3 urns. What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?
"""


def calculateProbability(S, A):
    print(len(A) / len(S))


if __name__ == "__main__":
    X = ["r", "r", "r", "r", "b", "b", "b"]
    Y = ["r", "r", "r", "r", "r", "b", "b", "b", "b"]
    Z = ["r", "r", "r", "r", "b", "b", "b", "b"]

    S = []
    for i in range(len(X)):
        for j in range(len(Y)):
            for k in range(len(Z)):
                S.append([X[i], Y[j], Z[k]])

    A = []
    for i in range(len(X)):
        for j in range(len(Y)):
            for k in range(len(Z)):
                rCount = 0
                bCount = 0

                if X[i] == "r":
                    rCount += 1
                else:
                    bCount += 1

                if Y[j] == "r":
                    rCount += 1
                else:
                    bCount += 1

                if Z[k] == "r":
                    rCount += 1
                else:
                    bCount += 1

                if rCount == 2 and bCount == 1:
                    A.append([X[i], Y[j], Z[k]])

    print(S)
    print(A)
    calculateProbability(S, A)