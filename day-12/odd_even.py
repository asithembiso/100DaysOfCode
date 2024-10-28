"""
Write a program to check if a number is even or odd.
"""


def odd_even(num: int):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


if __name__ == "__main__":
    my_num = 4
    print(odd_even(my_num))
