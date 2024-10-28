"""
Write a program to find the largest of three numbers.
"""
from typing import List


def largest(nums: List[int]):
    return max(nums)


if __name__ == "__main__":
    mylist = [12, 4, 58]
    print(largest(mylist))
