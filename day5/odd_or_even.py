"""
Write a program that reads an integer as user input and
prints whether the number is Odd or Even to the console
"""
my_num = int(input("Enter a number: "))

if my_num % 2 == 0:
    print(f"Your number {my_num} is Even")
else:
    print(f"Your number {my_num} is Odd")

