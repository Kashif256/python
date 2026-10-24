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


def func_26(name,age=20):
# def func_26(name, age):   In this condition we have to upload both name and age if we apply only one then it will shows an error like misssing one argument: 'age'
    print("name", name)
    print("age", age)
# func_26("Kash") in this we declare only age so it will pass an error
func_26("sanu", 19) # it will give the age as 19
func_26("Kash") # it will defaulty assign the age as 20 



# ------------- LAMDA FUNCTION ------------------
print("LAMBDA FUNCTION")

# A lambda function is a small anonymous function to make a developers life easier. Can take any number of arguments but only have one expression.

# SYNTAX =>     lamda arguments : expression 

# 1. create a lamda function that adds 10 with the number passed as an argument and print the result

x = lambda a: a+10
print("The value of a is +10 =", x(10))

# 2. Lamda function for finding odd or even

s = lambda a:"even" if a%2 == 0 else "odd"
print(s(10))