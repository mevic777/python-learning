fruits = ['apple', 'orange', 'banana', 'coconut']
vegetables = ['celery', 'carrots', 'potatoes']
meats = ['chicken', 'fish', 'tomato']

groceries = [fruits, vegetables, meats]

print(groceries)
print(groceries[0][0])
print(groceries[2][1])
print(groceries[2][0])
print(groceries[1][1])

for grocery in groceries:
    for food in grocery:
        print(food, end=", ")

print()

num_pad = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ('*', 0, '#'))

for row in num_pad:
    for column in row:
        print(column, end=" ")
    print()