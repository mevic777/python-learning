def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} old!")
    print()

happy_birthday("Bro", 29)
happy_birthday("Steve", 40)
happy_birthday("Joe", 20)

def display_invoice(username, amount, due_date):
    print(f"Hello, {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

display_invoice("Maverick_2025", 42.21, "01/05")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()

    return first + " " + last

full_name = create_name("marius", "covali")
print(full_name)

# these are positional arguments.
