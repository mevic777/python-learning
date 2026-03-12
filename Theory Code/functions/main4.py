# ARBITRARY ARGUMENTS
# *args = allows to pass multiple arguments non-key arguments -> tuple
# *kwargs = allows to pass multiple keyword-arguments

def add(*args):
    print(type(args))

    total = 0

    for arg in args:
        total += arg
    
    return total

total = add(1, 2, 3, 4, 5, 6, 6)
print(total)


def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Marius", "Covali", "Sergiu")


def print_address(**kwargs):
    print(type(kwargs))
    
    for key, value in kwargs.items():
        print(f"{key} - {value}")

print_address(street="123 Fake St.", city="Chisinau", zipcode="2020")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    for key, value in kwargs.items():
        print(f"{key}: {value}")

    if "apt" in kwargs:
        print(kwargs.get('street'))
        print(kwargs.get('apt'))
    else: 
        print(kwargs.get('street'))
        print(kwargs.get('pobox'))
    print(kwargs.get('city'))

shipping_label("Dr.", "Spongebob", "Square Pants", "The third", street="123 Fake St.", pobox="1501", city="Chisinau", zipcode="2020", apt="101")