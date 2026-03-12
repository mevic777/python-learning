# Class methods = Allows operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself
# Best for class level data or require access to the class itself

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} - {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count:.2f}"
    

student1 = Student("Marius", 3.2)
student2 = Student("Alex", 3.0)
student3 = Student("Valeria", 4.0)
student4 = Student("Ion", 2.9)
student5 = Student("Vasile", 1.0)

print(Student.get_count())
print(Student.get_gpa())