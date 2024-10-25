"""
Write a program that takes three numbers as input and prints the largest among them
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

"""
Easy way

my_nums = [num1, num2, num3]
print(max(my_nums))

"""

if num1 > num2 and num1 > num3:
    print(f"{num1} is the largest.")
if num2 > num1 and num2 > num3:
    print(f"{num2} is the largest.")
if num3 > num1 and num3 > num2:
    print(f"{num3} is the largest.")
