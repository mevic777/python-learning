import numpy as np

array = np.array([1.91, 2.54, 3.32])

# Basic scalar arithmetic
print(array + 1) # here comes arithmetic from np, where it just modify all the data
print(array - 2)
print(array * 5)
print(array / 2)
print(array ** 5)

# Vectorized math functions

print(np.sqrt(array))
print(np.round(array))
print(np.floor(array))
print(np.ceil(array))

# Exercise
radiuses = np.array([1, 2, 3])
print(np.ceil(np.pi * radiuses ** 2))

# Element-wise arithmetic
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2) # it does math operations element by element
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

# Comparison operators
scores = np.array([91, 55, 100, 73, 82, 64])
print(scores == 100)
print(scores >= 60)
print(scores < 60)

scores[scores < 60] = 0 # -> we select all the values from our array that are less than 60
print(scores)