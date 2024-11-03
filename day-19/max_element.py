"""
Write a function to find the maximum element in a list.
"""


def max_element(elements: [int]) -> int:
    maximum = 0
    for element in elements:
        if element >= maximum:
            maximum = element
    return maximum
    # return max(elements) using built in function


if __name__ == "__main__":
    my_list = [1585, 98, 100, 157, 58, 7, 1000, 0, -5]
    print(max_element(my_list))
