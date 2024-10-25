"""
Create a simple calculator program that can add, subtract, multiply, and divide two integers
"""

operation = int(input("Choose operation:\n1.Add\n2.Subtract\n3.Multiply\n4.Devide\n\n"))
print()
if operation == 1:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    print(f"\nAnswer is {first_number+second_number}")

if operation == 2:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    print(f"\nAnswer is {first_number-second_number}")

if operation == 3:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    print(f"\nAnswer is {first_number*second_number}")

if operation == 4:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))
    print(f"\nAnswer is {first_number/second_number}")