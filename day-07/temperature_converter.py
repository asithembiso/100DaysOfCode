"""
1. Write a program to convert temperature from Celsius to Fahrenheit.
2. Write a program to convert temperature from Fahrenheit to Celsius

"""


def celsius_to_fahrenheit(temp: float) -> float:
    return (temp * (9/5)) + 32


def fahrenheit_to_celsius(temp: float) -> float:
    return (temp - 32) * (5/9)


print(celsius_to_fahrenheit(20))
print(fahrenheit_to_celsius(68))
