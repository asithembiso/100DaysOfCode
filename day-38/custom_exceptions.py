"""
Create a custom exception class.
"""

class CustomException(Exception):
    pass


try:
    i = 1
    if i < 2:
        raise CustomException
    else:
        print("No exception")
except CustomException:
    print("Custom exception error")
