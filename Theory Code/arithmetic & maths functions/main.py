x = 3.15
y = 4
z = 5

result = round(x) # 3.15 -> 3
result2 = abs(y) # 4 -> -4
result3 = pow(y, 3) # 4 * 4 * 4
result4 = max(x, y, z) # the max value
result5 = min(x, y, z) # the min value

import math

print(math.pi) # pi number
print(math.e) # e number

result6 = math.sqrt(y) # radical din y = 4 -> 2
result7 = math.ceil(x) # round to 4
result8 = math.floor(x) # round to 3

radius = int(input("Enter the radius of a circle: "))
c = 2 * math.pi * radius

print(f"Circle length is: {c} or {math.ceil(c)}")

area = math.pi * pow(radius, 2)

print(f"Area is: {area} or {math.floor(area)}")

a = int(input("Side A: "))
b = int(input("Side B: "))

hypothenus = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Hypothenus is: {hypothenus} or {math.floor(hypothenus)}") 