# Basic arithmetic
num1 = 5
num2 = 10
ans = num1 * num2 + num1 - num2*3
print(ans)

# Calculate the area of a rectangle A = l * w
length = 15
width = 3
area = length * width
print(area)

# Area of rectangle with input
length = float(input("Enter length: "))
width = float(input("Enter width: "))
# Precision to two decimal points
area = round(length*width, 2)

print(f"The area of your rectangle Area = {length} * {width} is {area}")
