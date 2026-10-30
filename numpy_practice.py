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

