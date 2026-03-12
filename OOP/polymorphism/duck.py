# Duck typing = Another way of polymorphism
#               Object must have the minimum necessary atribues / methods
#               "If it quacks like a duck and act like a duck, it must be a duck"

class Animal:
    
    alive = True

class Dog(Animal):
    
    def speak(self):
        print("WOOF")

class Cat(Animal):
    
    def speak(self):
        print("Meow")

class Car():
    
    alive = False

    def speak(self):
        print("Honk")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
