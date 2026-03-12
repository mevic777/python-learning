# Iterables = An object/collection that can return its elements one at a time
# allowing it to be iterated over a loop


numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number)

numbers2 = (1, 2, 3, 4, 5)

for number in numbers2:
    print(number)

numbers3 = {1, 2, 3, 4, 5}

for number in numbers3:
    print(number)

name = "Bro Code"

for character in name:
    print(character, end=" ")

my_dictionary = {
    "name": "Marius",
    "surname": "Covali"
}

for key, value in my_dictionary.items():
    print(key, value)

