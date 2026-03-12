# Hashsets
s = set()
print(s)

s.add(1)
s.add(2)
s.add(3)

print(s)

if 1 not in s:
    print(True)

s.remove(3)

print(s)

a = "aaaaaaaaaaaabbbbbbbbbbbbbbbbbeeeeeeeeeeeee" 
sett = set(a)

print(sett)

for x in s:
    print(x)

# Hashmaps

d = {'greg': 1, 'steve': 2, 'rob': 3}
print(d)

d['arsh'] = 4
print(d)

# Check if a key is in the hashmap - O(1)
if 'greg' in d:
    print(True)

# Check the value corresponding to the key - O(1)
print(d['greg'])

# Loop over the key value pair
for key, value in d.items():
    print(f"{key}: {value}")

# Default dict
from collections import defaultdict

default = defaultdict(int)
print(default[2])

# Counter
from collections import Counter

counter = Counter(a)
print(counter)