name = input("What is your name?: ")
age = int(input("How old are you?: "))

# age = int(age)
# age = int(age) + 1
age = age + 1

print(f"Hello {name}")
print("Happy Birthday")
print(f"You are {age} years old")

# Exercise 1 Rectangle Area Calc
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))

area = length * width

print(f"Area: {area}")

# Exercise 2 Shopping Cart Program
item = input("What item would you like to buy?:")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))

total = price * quantity

print(f"You have bought {quantity} x {price}.")
print(f"Your total is: {total}")