# class variables = Shared among all instances of a class
#                   Defined outside the constructor 
#                   Allow you to share data among all objects created from class

class Student:
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student2 = Student("Squidward", 55)
student2 = Student("Sandy", 27)

print(student1.name)
print(student1.age)

# This is good practice so we know that it has such property
print(Student.num_students)
print(Student.class_year)
