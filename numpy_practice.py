print("Numpy")

# NumPy (Numerical Python) is a Python library used to perform mathematical and numerical operations on large amounts of data efficiently.

# FOR INTEGER
 
import numpy as np

a = np.array([[1, 2, 3]])

print(a)
print(type(a))

# float

import numpy as np
b = np.array([1.5,2.0,3.1], dtype = float)
print(b)
print(type(b))


c= np.array([[1,2,3],[4,5,6]])
print(c)
print(len(c))
print(c.ndim) # o/p=> 2, because the array has two dimensions: rows and columns.


# A company gives you its sales data for five days.

import numpy as np

sales = np.array([1000, 2000, 3000, 4000, 5000])

print("Total Sales:", np.sum(sales))  # 15000
print("Average Sales:", np.mean(sales)) # 3000.0
print("Highest Sales:", np.max(sales)) # 5000
print("Lowest Sales:", np.min(sales)) # 1000



# ACCESING / CHANGING SPECIFIC ELEMENTS, ROWS & COLUMNS 

s = np.array([[1,2,3,4,5,6,7,8],[9,10,11,12,13,14,15,16]])
print(s)

# to print specific term  [row, column]
print(s[1,2]) # 12

# to get a row
print(s[0,:])

# get a specific column from a numpy array
print(s[:,0]) # o/p => 1 9

# change value
s[1,2] = 40
print(s)  # o/p =>  [ 9 10 40 12 13 14 15 16]]


print("Zeros / ones methods in python")

k = np.zeros((3,3))
print(k)   # o/p => will be in float format

k = np.zeros((3,3), dtype = 'int32')
print(k)  # it will be in integer

k = np.zeros((3,3), dtype = 'str')
print(k)  # it will be in string

# for one also similar like zeros

l= np.ones((3,3))
print(l)   # o/p => will be in float format

# to print a particular number

m = np.full((3, 3), 50, dtype = 'int32')
print(m)

# to print a random number

n = np.random.rand(4,4)
print(n)

# to print random integer in a particular range 

o = np.random.randint(-4,1, size=(3,3))
print(o)

# to print the identity matrix

p = np.identity(3)
print(p)