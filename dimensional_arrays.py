import numpy as np

array = np.array('A') # -> zero dimensional array
print(array.ndim) # -> this offer us the number of dimension of the array

array1 = np.array(['A', 'B', 'C']) # -> one dimensional array
print(array1.ndim)

array2 = np.array([['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]) # -> 2 dimensional array
print(array2.ndim)

array3 = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                   [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                   [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]]) # -> 3 dimensional array
print(array3.ndim)
print(array3.shape) # -> offers us a tuple (3, 3, 3), first is depth (nr. of layer), nr. of rows, and nr. of cols
print(array3[0][0][0]) # -> chain indexing
print(array3[0, 0, 0]) # -> multidimensional indexing (from numpy), cause it is a lot faster

word = array3[0, 0, 0] + array3[1, 2, 1] + array3[2, 0, 1] # -> AHB
print(word)