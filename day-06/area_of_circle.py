"""
Write a program that takes radius of the circle and outputs the area of the circle to 2 decimal digits
"""
import math

radius = float(input("Enter radius of circle: "))

diameter = 2 * radius

area = math.pi * (diameter/2)**2

print(f"Area = {area:.2f}")
