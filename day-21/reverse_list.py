"""
Write a function to reverse a list.
"""
from typing import List


def reverse(mylist: List) -> List:
    tmp = []
    i = len(mylist) - 1
    while i >= 0:
        tmp.append(mylist[i])
        i -= 1
    return tmp


if __name__ == "__main__":
    var = [7, 8, 9, 7, 1]
    print(reverse(var))
