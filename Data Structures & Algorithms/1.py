A = [1, 2, 3]
print(A)

# Append - Insert element at the end - On avg: O(1)
A.append(5)
print(A)

# Pop - Delete element from the end - On avg: O(1)
A.pop()
print(A)

# Insert - get acces from a specific position - On avg: O(n)
A.insert(2, 8)
print(A)

# Modify - On avg: O(1)
A[0] = 7
print(A)

# Accesing an element from the list
print(A[0])

# Check if a value is in the Array - On avg: O(n)

if 7 in A:
    print(True)

# Append at the of string - O(n)
s = 'hello'
b = s + 'z'
print(b)

# Check if something is in the string - O(n)
if 'e' in s:
    print(True)

# Acces different position in the string - O(1)
print(s[2])

# Get the length of the string - O(1)
lenght = len(s)