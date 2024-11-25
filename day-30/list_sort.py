"""
Sort a list of numbers in ascending order
"""
from typing import List


def sort_list(arr: List) -> List:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] <= arr[j]:
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp
    return arr


if __name__ == "__main__":
    mylist = [5, 9, 1, 3, 8, 4]
    print(sort_list(mylist))
