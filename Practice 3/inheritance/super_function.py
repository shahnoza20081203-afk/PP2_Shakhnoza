class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog says Woof")

dog1 = Dog()
dog1.sound()

#2
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, university):
        super().__init__(name)
        self.university = university

student1 = Student("Tumar", "KBTU")

print(student1.name)
print(student1.university)

#3
class Person:
    def introduce(self):
        print("My name is a person")

class Student(Person):
    def introduce(self):
        super().introduce()
        print("I am a student")

student1 = Student()

student1.introduce()

#4
class Employee:
    def show_info(self):
        print("I am an employee")

class Manager(Employee):
    def show_info(self):
        super().show_info()
        print("I am a manager")

manager1 = Manager()
manager1.show_info()