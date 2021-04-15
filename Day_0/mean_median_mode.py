"""
Author: Charles Herrmann
Date: 4/13/21
Objective: In this challenge, we practice calculating the mean, median, and mode.
Task: Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.
"""

import sys

# Get input from stdin
n = int(input())
a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
a.sort()

# Calculate mean
mean = sum(a) / n

# Calculate median
if n % 2 == 0:
    median = (a[int((n / 2) - 1)] + a[int(n / 2)]) / 2
else:
    median = a[int(n / 2)]

# Calculate mode
count = {}
for i in a:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

maxOccur = 0
mode = 0
for key in count.keys():
    if count[key] > maxOccur:
        mode = key
        maxOccur = count[key]

# Print results
print(mean)
print(median)
print(mode)