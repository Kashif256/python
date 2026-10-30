print(" map reduce filter")

# Definition: map() applies a function to every item in a collection.
#syntax => map(function, iterable)


# example program which multiplies 2 with the number

numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)


radius = [1,2, 3, 4]
circumtance = list(map(lambda radius: 3.14 * radius**2 , radius))
print(circumtance)


print("with use of import math") 

import math
def area(r):
    return 3.14*(r**2)
radii = [1,2,3,4]
areas = []
circum = list(map(area, radii))
print(circum)


# convert celcius scale to farhenheit scale

temp = [('Mumbai' , 30) , ('Delhi', 25), ('Chennai', 20)]
fahrenhit = list(map(lambda data: (data[0], 9/5 * data[1] +  32), temp))
print(fahrenhit)

# without using map and lambda function 

float = int(input("Enter the celcius temperature: "))
fahrenheit = 9/5 * float + 32
print("The temperature in fahrenheit is: ", fahrenheit)




# ----------------------------------------------------filter function--------------------------------------------------------

# Definition: filter() selects items that satisfy a given condition.
#syntax => filter(function, iterable)

import statistics
data = [1, 2, 3, 4, 5, 6, 7, 8, 9,2,1,12,11]
avg = statistics.mean(data)
my_filter = list(filter(lambda x: x> avg , data))
print(my_filter)


print("MAP & FILTER")

# in this it calls the value from the 6th line and filter it based on greater than 10.
sanu = list(filter(lambda x: x > 10, circum))
print(sanu)  # [12.56, 28.26, 50.24]


print("To reduce the 0 nd empty values")
num=[1,2,3,4,0,0,6,"",5]
my_filter_26 = list(filter(lambda x:x!=0 and x!="", num))
print(my_filter_26)  #[1, 2, 3, 4, 6, 5]



# Reduce function

print ("Reduce function")

# Definition: reduce() combines items in a collection to produce a single result.
# syntax => from functools import reduce
#           reduce(function, iterable)

from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)



# multiply all the items in a list

from functools import reduce
data_26 = [1,2,3,4,5,6]
result_26 = reduce(lambda x, y: x*y, data_26)
print(result_26)    # output => 720


# without lambda function

data_26 = [1,2,3,4,5,6]
prev = data[0]
for i in data_26:
    i = i*prev
    prev = i
print (prev)  # output => 720


# sum all the items in a list

from functools import reduce
data_26 = [1,2,3,4,5,6]
result_26 = reduce(lambda x, y: x+y, data_26)
print(result_26)