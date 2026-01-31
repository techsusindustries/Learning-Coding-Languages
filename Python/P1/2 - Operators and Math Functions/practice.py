# Addition operator  
# Subtraction operator  
# Multiplication operator  
# Division operator  
# Exponentiation operator  
# Modulus operator  
# Using modulus to check even/odd  
# Rounding numbers  
# Absolute value  
# Power function  
# Finding maximum value  
# Finding minimum value  
# Importing modules  
# Using mathematical constants (pi)  
# Square root function  
# Ceiling function  
# Floor function

# Import dependencies
import math

# Get numbers from input
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

# Built in operators and functions
print("-- Built-in Operators and Functions --")
print(f"The sum of {x} and {y} is: {x + y}")
print(f"The difference when {y} is subtracted from {x} is: {x-y}")
print(f"The product of {x} and {y} is: {x * y}")
print(f"The quotient when {x} is divided by {y} is: {x / y}")
print(f"{x} raised to the power of {y} is: {x ** y}")
print(f"The remainder when {x} is divided by {y} is: {x % y}")
print(f"{x}, 0 for even, 1 for odd: {math.floor(x) % 2}")
print(f"{y}, 0 for even, 1 for odd: {math.floor(y) % 2}")
print(f"{x} rounded to the nearest 100th is: {round(x, 2)}")
print(f"{y} rounded to the nearest 100th is: {round(y, 2)}")
print(f"The absolute value of {x} is: {abs(x)}")
print(f"The absolute value of {y} is: {abs(y)}")
print(f"{x} raised to the power of {y} using pow() is: {pow(x,y)}")
print(f"{x} raised to the power of {y} using ** is: {x ** y}")
print(f"The maximum of {x} and {y} is: {max(x,y)}")
print(f"The minimum of {x} and {y} is: {min(x,y)}")

# Math module functions
print("-- Math Module Functions --")
print(f"The value of pi rounded to the nearest 100th is: {round(math.pi, 2)}")
print(f"The square root of {x} is: {math.sqrt(x)}")
print(f"The square root of {y} is: {math.sqrt(y)}")
print(f"{x} rounded up to the nearest integer is: {math.ceil(x)}")
print(f"{x} rounded down to the nearest integer is: {math.floor(x)}")
print(f"{y} rounded up to the nearest integer is: {math.ceil(y)}")
print(f"{y} rounded down to the nearest integer is: {math.floor(y)}")

# Circle calculations
print("-- Circle Calculations --")
r = float(input("Enter the radius of your circle: "))
carea = math.pi * (r ** 2)
circum = 2 * math.pi * r
print(f"The area of a circle with radius {r} is: {carea}")
print(f"The circumference of a circle with radius {r} is: {circum}")

# Right Triangle calculations
print("-- Right Triangle Calculations --")
b = float(input("Enter the base of your triangle: "))
h = float(input("Enter the height of your triangle: "))
tarea = 0.5 * b * h
hyp = math.sqrt(b**2 + h**2)
print(f"The area of a triangle with base {b} and height {h} is: {tarea}")
print(f"The hypotenuse of a triangle with base {b} and height {h} is: {hyp}")