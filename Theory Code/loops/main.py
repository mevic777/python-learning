name = input("Enter your name: ")

while name == "":
    print("You did not enter your name")
else:
    print(f"Hello, {name}")

age = int(input("Enter an age: "))

while age < 0:
    print("Age cannot be negative")
    age = int(input("Enter an age: "))

print(f"You are {age} years.")

food = input("Enter a food you like (q to quit)")

while not food == 'q':
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit)")

print("bye")

num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")