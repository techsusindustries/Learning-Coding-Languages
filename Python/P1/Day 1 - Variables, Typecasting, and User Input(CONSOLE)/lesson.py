# 1/3 today, Variables

# Four data types for variables: string, integer, float, boolean

# Strings(Text)
greeting = "wsg"
name = "brochacho"

# Placing f before the quotes allow you to use brackets to include variables easily
print(f"{greeting} fellow bro")
print(f"Your name is {name}")

# Integers(Standard Numbers)
weight = 69
numOfRubberDucks = 10000

print(f"You weigh {weight} lbs")
print(f"You have {numOfRubberDucks} Rubber Duckies")

# Floats(Decimal Numbers)
netWorth = 0.55
gpa = 3.7

print(f"You have a net worth of {netWorth}")
print(f"Your GPA is {gpa}")

# Booleans(True/False)
# First letter is capital
hasRizz = False

print(f"Do you have rizz? {hasRizz}")

# 2/3 today, Typecasting

# Four functions to convert between variable types:
# str(), int(), float(), bool()

print(type(gpa)) # Float
print(type(weight)) # Integer
print(type(greeting)) # String
print(type(hasRizz)) # Bool

# GPA is truncated from 3.7->3
gpa = int(gpa)
print(gpa)
print(type(gpa)) # Integer

# Weight now has decimal capabilities
weight = float(weight)
print(weight)
print(type(weight)) # Float

# RDucks can now play with strings(No longer number capable)
numOfRubberDucks = str(numOfRubberDucks)
print(numOfRubberDucks)
print(type(numOfRubberDucks)) # String

# Empty Strings are false, populated strings are true
string1 = ""
string2 = "I am a string"
string1 = bool(string1)
string2 = bool(string2)
print(string1) # Boolean
print(string2) # Boolean

# 3/3 today, User Input(CONSOLE)

# User Input can be used for variables, the question if any goes in the inputs ()
# User Input is stored as a string variable, convert to int or float for math

ssn = input("Whats your social security number?: ")
age = input("Whats your age?: ")
agep1 = int(age) + 1

print(f"Your SSN is: {ssn}")
print(f"Your age is: {age}")
print(f"Your age + 1 is: {agep1}")

# Calc area of rectangle example
length = float(input("Enter the ft length: "))
width = float(input("Enter the ft width: "))
area = length * width

print(f"The area is: {area}ft")
print(f"The area is: {length * width}ft") # More efficient for in () math if a result is not important anywhere else

# Shopping Cart Example
item = input("What are you buying?: ")
price = float(input("Whats its price?: "))
quantity = int(input("How many of them are you buying?: "))
total = price * quantity

print(f"You are buying {quantity}x {item} for ${total}")