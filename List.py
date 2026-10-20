# list

# list are used to store multiple values in a single variable and it is closed inside the [] square brackets and separated by commas and list are mutable

list1 = [1,2,3,4,5]
print(list1)
print(type(list1))  # o/p => <class 'list'>

# combination of multiple values in a single variable

list2 = [1,"Kash", 12.5, True, ["Sanu", 6], 4]
print(list2)
print(len(list2))   # o/p => 6
print(type(list2))  # o/p => <class 'list'>

# Mutability

list3 = [1,2,3,4,5]
list3[0] = 10
print(list3) # o/p => [10, 2, 3, 4, 5]

# extend 

list4 = [1,2,3,4,5]
list4.extend([6,7,8,9,10])
print(list4 ) # o/p => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# del 

list5 = [1,2,3,4,5]
del list5[0]
print(list5) # o/p => [2, 3, 4, 5]

# pop

fruits = ["Apple", "Mango", "Banana"]
fruits.pop(1)
print(fruits)  # o/p => ['Apple', 'Banana']

# remove

fruits = ["Apple", "Mango", "Banana"]
fruits.remove("Mango")
print(fruits)  # o/p => ['Apple', 'Banana']

# sort

list6 = [8,4,9,2,0,4]
list6.sort()
print(list6)  # o/p => [0, 2, 4, 4, 8, 9]

# sorted => it will return a new list and it will not change the original list

list7 = [8,4,9,2,0,4]
list8 = sorted(list7)
print(list8)  # o/p => [0, 2, 4, 4, 8, 9]
print(list7)  # o/p => [8, 4, 9, 2, 0, 4]

# shallow copy => it will create a new list but it will not create a new object and it will point to the same object

a = [1,2,3,40,5]
b = a.copy()
b.append(6)
print("a's original value is : " ,a )  # o/p => a's original value is :  [1, 2, 3, 40, 5]
print("b's value is : " ,b )  # o/p => b's value is :  [1, 2, 3, 40, 5, 6]