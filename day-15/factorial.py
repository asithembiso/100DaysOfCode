"""
Write a function to calculate the factorial of a number.
"""


def factorial(n: int):
    if n < 1:
        return 1
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact


if __name__ == "__main__":
    print(factorial(7))
    print(factorial(0))
    print(factorial(1))

