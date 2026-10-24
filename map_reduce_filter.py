print(" map reduce filter")

# Definition: map() applies a function to every item in a collection.
#syntax => map(function, iterable)


# example program which multiplies 2 with the number

numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)


# Definition: reduce() combines items in a collection to produce a single result.
# syntax => from functools import reduce
#           reduce(function, iterable)

from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
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
filter = list(filter(lambda x: x> avg , data))
print(filter)