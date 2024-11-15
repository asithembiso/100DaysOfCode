"""
Write a function to find the intersection of two lists.
"""
from typing import List


def intersection(list_one: List, list_two: List) -> List:
    if len(list_one) < 1 or len(list_two) < 1:
        return []
    intersect = []
    for item in list_one:
        if item in list_two:
            intersect.append(item)
    return intersect


if __name__ == "__main__":
    list1 = [1, 5, 7, 9, 0]
    list2 = [2, 1, 7, 0]
    print(intersection(list1, list2))
