# An iterable is an object that contains multiple items that we can go through one by one.
# Examples include:
#- List - Tuple - String - Dictionary - Set

# An iterator is an object that gives us items one at a time when we ask for them.
#We can create an iterator from an iterable using iter() and get the next item using next().

# if else block 

a = int(input("Enter a number: "))
if( a % 2 == 0):
    print("it is even")
else:
    print("it is odd")

b = int(input("Enter your age : " ))
name = input("Enter your name : ")
if(b > 18):
    print(name + ", you are eligible")
else:
    print(name + ", you are not eligible") 

# using elif statement

shopping = int(input("Enter ur bill amount : "))
if( shopping >= 5000):
    print("you have an vouncher of 1000")
elif(shopping >= 2500):
    print ("you have an voucher of 500")
else:
    print("Sorry you dont have any vouncher")



# ------------------  ITERATED OVER A LIST OF VALUES ------------------

list_1 = [1,2,3,4,5,6,7,8]
for i in list_1:
    print(i)



# ------------------  ITERATED OVER A STRING ------------------

str = " Saniya"
for i in str:
    print(i)


# ------------------  ITERATED OVER A DICTIONARY ------------------

student_data = { 1: ["kash", 21], 2:["sanu", 20]}
for i in student_data:   # with this it gives only the key only
    print(i)


student_data1 = {1: ["kash", 21], 2: ["sanu", 20]}
for i in student_data.items(): # it gives the key and values both
    print(i)


student_data2 = {1: ["kash", 21], 2: ["sanu", 20]}
for i,j in student_data2.items(): # in this it gives only the pair value
    print(j)



# ------------------ COMPREHENSION ------------------

data = ["kash", "sanu", "saniya", "kash"]
students = {i + 1: name for i, name in enumerate(data)} # it gives the keys for the value in the list
print(students)
d = { i: len(i) for i in data} # it gives the length of each name in the list
print(d)