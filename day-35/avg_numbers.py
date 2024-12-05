"""
Calculate the average of numbers in a text file.
"""

import os

cwd = os.getcwd()
numbers = []

with open(cwd + "/numbers.txt", "r") as file:
    nums = file.read()
    for num in nums.split():
        numbers.append(int(num))
    average = sum(numbers)/len(numbers)
    print(average)
