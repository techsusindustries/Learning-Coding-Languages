# 1/3 Today, Conditionals

age = int(input("Enter your age: "))

# If statement, format: if variable (operator) value: Supported operators: == Equal to, != Not equal to, < Less than, > Greater than, <= Less than or equal to, >= Greater than or equal to
# Indenting is very important for if statements, use 4 spaces or a tab per indent level
if age >= 80:
    print("You old bro.")
elif age >= 18:
    print("You are an adult.")
elif age <= 0: # An alternative if statement if the first if statement is false, can be used multiple times
    print("Bro was born on his birthday :skull:.")
else: # Runs if the if statement is false, self explanatory
    print("You are a minor.")

# Another example
hasRizz = input("Do you have rizz? (y/n): ")

if hasRizz == "y":
    print("Your have rizz.")
    hasRizz = True
elif hasRizz == "n":
    print("You have no rizz.")
    hasRizz = False
else:
    print("We dont know if you have rizz or not.")

# Part 2 of last example with booleans
print("Checking rizz status...")
if hasRizz == True: # When using only true specifically, it can be shortened to just "if hasRizz:"
    print("You were able to rizz up the lady")
else:
    print("You were not able to rizz up the lady")

# 2/3 Today, Logical Operators

# Supported operators:
# or - at least one condition is true
# and - all conditions are true
# not - true if the condition is false and vice versa
# Seperate multiple conditions with logical operators, combining multiple logical operators is possible if needed
temp = 25
is_raining = True

if temp > 20 and not is_raining:
    print("It's a nice day outside!")
else:
    print("It's not a nice day outside.")

a = 0
b = 5
c = True

# It is recommended to use parentheses to make the order of operations clearer, but they are not required
if (a != 0 or (b == 5 and c)):
    print("At least one of the conditions is true.")

# Similar to math, you can simplify ranges using a chain inequality
if (20 > b > 0):
    print("b is between 0 and 20")

# 3/3 Today, Conditional Expressions

# Conditional Expressions are a one line version of an if-else statement(no elif support)
num = -5

# There are multiple ways to use a conditional expression, ex:
print("Positive" if num > 0 else "Negative or Zero") # Within a single function
print("Positive") if num > 0 else print("Negative or Zero") # With separate functions
result = "Positive" if num > 0 else "Negative or Zero" # Assigning to a variable
# At its core the format is: valueiftrue if condition else valueiffalse