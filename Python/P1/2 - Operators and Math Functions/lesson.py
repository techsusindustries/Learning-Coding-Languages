# Addition operator
friends = 0

friends = friends + 1
print(friends)

friends += 1 # You can use (operater)= to do something with a number while assigning it in the same step(Shorter way)
print(friends)

# Subtraction operator
friends -= 2
print(friends)

# Multiplication operator
friends *= 3
print(friends)

# Division operator
friends /= 2
print(friends) # Results in a float

# Power of operator
friends **= 3 # The number after the power operator is the power the number will be raised to
print(friends)

# Modulus operator(Remainder of division)
friends = 10

remainder = friends % 3
print(remainder)
# Note: Using 2 as the divisor will tell you if a number is even or odd. If the remainder is 0, the number is even. If the remainder is 1, the number is odd

# Math functions
x = 3.14
y = -4
z = 5

result1 = round(x) # Rounds the number to the nearest integer
print(result1)

result2 = abs(y) # Returns the absolute value of the number
print(result2)

result3 = pow(4, 3) # Raises the first number to the power of the second number
print(result3)

result4 = max(x, y, z) # Returns the largest number among the given numbers
print(result4)

result5 = min(x, y, z) # Returns the smallest number among the given numbers
print(result5)

# For the next math functions, we need to import the math module
import math

w = 9

print(math.pi) # Prints the value of pi
print(math.e)  # Prints the value of e(idk what e is but its a math constant)
result6 = math.sqrt(w) # Returns the square root of the number
print(result6)
result7 = math.ceil(x) # Rounds the number up to the nearest integer
print(result7)
result8 = math.floor(x) # Rounds the number down to the nearest integer
print(result8)

# Calculating the area of a circle example
radius = float(input("Enter the radius of the circle: "))
circum = 2 * math.pi * radius
print(f"The circumference of the circle is: {round(circum, 2)}cm") # The second value lets your round to a certain number of decimal places

# Calculating the area of a circle example
area = math.pi * math.pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)}cm²")

# Calculating the hypotenuse of a right triangle example
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
print(f"The length of the hypotenuse is: {round(c, 2)}cm")