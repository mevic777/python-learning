# Broadcasting allows numpy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape

# The dimensions should be the same size
# OR
# One of the dimensions has a size of 1

import numpy as np

array1 = np.array([[1, 2, 3, 4]])
array2 = np.array([[1], 
                   [2], 
                   [3], 
                   [4]])

# we read the dimensions from right to left
# and either one of them should have value 1 
# or have the same number
# In our case it respects all the rules so we can broadcast them
print("First example")
print(array1.shape)
print(array2.shape)

print(array1 * array2)

print("\nSecond example")
array1 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])
array2 = np.array([[1], 
                   [2], 
                   [3], 
                   [4]])


print(array1.shape)
print(array2.shape)

print(array1 * array2)