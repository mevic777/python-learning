# Decorator = a function that extends the behavior of another function
#             w/o modifying the base function
#             Pass the base function as an argument to the decorator

# syntax for decorator

# def add_sprinkles(func):
#     def wrapper():
#         func()
    
#     return wrapper

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles")
        func(*args, **kwargs) # -> print("Here is your ice cream")
    
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)

    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your ice cream {flavor}")

get_ice_cream("vanilla")

