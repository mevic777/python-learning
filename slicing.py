import numpy as np

array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12], 
                  [13, 14, 15, 16]])

# subscript operator: array[start:end:step]
print("Row selection")
print("From second till last")
print(array[1:4])

print("\nSame but in another way\n")
print(array[:4])

print("\nSlicing every 2 rows from the the all array\n")
print(array[0:4:2])

print("\nSame but another way\n")
print(array[::2])

print("\nAll but reversed\n")
print(array[::-1])

print("\nColumns selection\n")
print(array[:, :3])

print("\nColumn from 2 to 4")
print(array[:, 1:4])

print("\nEvery second columns")
print(array[:, ::2])

print("\nEvery second columns but starting column 1")
print(array[:, 1::2])

print("\nCombination of rows and columns selection")
print(array[0:2, 0:2])
print(array[0:2, 2:4])
print(array[2:4, 0:2])
print(array[2:4, 2:4])