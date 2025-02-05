"""
Handle exceptions for division by zero

"""

def division(first: int, second: int) -> float:
    try:
        return first / second
    except ZeroDivisionError as err:
        print(err)


if __name__ == "__main__":
    first = 1
    second = 0
    print(division(first,second))
