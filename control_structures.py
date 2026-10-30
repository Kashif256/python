# Definition:
# Control structures are statements that control the flow
# and execution of a Python program.

# They decide which code should execute,
# how many times it should execute, and when it should stop.

# There are 3 main types of control structures:

# 1. Sequential Control Structure
# 2. Selection / Decision Control Structure
# 3. Iteration / Looping Control Structure


# 1. Sequential Control Structure
# Definition:
# Statements are executed one after another in order.

a = 10
b = 20
c = a + b

print(c)

# Output: 30


# 2. Selection / Decision Control Structure
# Definition:
# It executes code based on a given condition.
# Examples: if, elif, else.

age = 21

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Output: Eligible to vote


# 3. Iteration / Looping Control Structure
# Definition:
# It executes a block of code repeatedly.
# Examples: for loop and while loop.

for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5


# Definition:
# Binary operators are operators that work with two operands
# (two values or variables) to perform an operation.

# Example:
# a + b
# Here, a and b are two operands.
# + is the binary operator.


# 1. Arithmetic Operators
# Used to perform mathematical calculations.

a = 10
b = 3

print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.333...
print(a // b) # Floor Division: 3
print(a % b)  # Modulus (remainder): 1
print(a ** b) # Exponentiation: 1000


# 2. Assignment Operators
# Used to assign or update values in variables.

x = 10

x += 5  # Same as x = x + 5
print(x) # 15

x -= 2  # Same as x = x - 2
print(x) # 13

x *= 2  # Same as x = x * 2
print(x) # 26

x /= 2  # Same as x = x / 2
print(x) # 13.0


# 3. Logical Operators
# Used to combine or reverse conditions.
# and, or, not

a = 10
b = 20

print(a > 5 and b > 10) # True
print(a > 15 or b > 10) # True
print(not(a > 5))       # False


# Definition:
# Relational operators are used to compare two values.
# They return either True or False.

a = 10
b = 20

# 1. Equal to (==)
# Checks whether two values are equal.

print(a == b)
# Output: False


# 2. Not equal to (!=)
# Checks whether two values are different.

print(a != b)
# Output: True


# 3. Greater than (>)
# Checks whether the left value is greater than the right value.

print(a > b)
# Output: False


# 4. Less than (<)
# Checks whether the left value is smaller than the right value.

print(a < b)
# Output: True


# 5. Greater than or equal to (>=)
# Checks whether the left value is greater than or equal to the right value.

print(a >= b)
# Output: False


# 6. Less than or equal to (<=)
# Checks whether the left value is smaller than or equal to the right value.

print(a <= b)
# Output: True