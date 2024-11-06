"""
Write a function to calculate the Fibonacci sequence up to a certain limit.
"""


def fibonacci(n: int):
    num1 = 0
    num2 = 1
    next_number = num1
    count = 1

    while count <= n:
        print(next_number, end=" ")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2
    print()


if __name__ == "__main__":
    num = 9
    fibonacci(num)
