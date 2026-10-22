# FUNCTION

# A function in Python works similarly. It is a reusable block of code that performs a particular task whenever you call it.


# Find odd or even using function

def odd_even(num):
    if num % 2 == 0:
        print(num, "It is even")
    else:
        print(num, "It is odd")

number = int(input("Enter a number: "))

print(odd_even(number))

# FACTORIAL OF A NUMBER

def fact_num(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

n = int(input("Enter a number for factorial: "))
print(fact_num(n))

# SUM OF NATURAL NUMBER

def natural_num(d):
    num = 0
    for i in range (1, d+1):
        num = num + i
    return num
print(natural_num(3))







# ------------- LAMDA FUNCTION ------------------

# A lambda function is a small anonymous function to make a developers life easier. Can take any number of arguments but only have one expression.

# SYNTAX =>     lamda arguments : expression 