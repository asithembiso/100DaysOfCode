"""
Write a function to find the sum of all elements in a list.
"""


def total(elements: [int]) -> int:
    itotal = 0
    for element in elements:
        itotal += element
    return itotal
    # return sum(elements) using built in sum function


if __name__ == "__main__":
    my_list = [1, 9, 99, 8, 4, 5]
    print(total(my_list))
