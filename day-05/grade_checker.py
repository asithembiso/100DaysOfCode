"""
Write a program that reads the percentage and
then prints their corresponding letter grade (A, B, C, D, or F)
"""

score = float(input("What is your test score? "))

if score >= 80:
    print("A+")
elif 70 <= score < 80:
    print("A")
elif 60 <= score < 70:
    print("B")
elif 50 <= score < 60:
    print("C")
elif 40 <= score < 50:
    print("D")
elif 30 <= score < 40:
    print("E")
else:
    print("F")
