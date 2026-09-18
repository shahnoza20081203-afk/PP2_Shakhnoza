#1
class Student:
    university = "KBTU"

student1 = Student()
student2 = Student()

print(student1.university)
print(student2.university)

#2
class Student:
    university = "KBTU"

student1 = Student()
student2 = Student()

Student.university = "Harvard"

print(student1.university)
print(student2.university)

#3
class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


student1 = Student("Ali")
student2 = Student("Sara")
student3 = Student("John")

print(Student.count)

#4
class Employee:
    company = "Kaspi"

    def __init__(self, name):
        self.name = name


employee1 = Employee("Aida")
employee2 = Employee("Daniyar")

print(employee1.name, employee1.company)
print(employee2.name, employee2.company)

#5
class Car:
    max_speed = 180

    def __init__(self, brand):
        self.brand = brand


car1 = Car("Toyota")
car2 = Car("BMW")

print(car1.max_speed)
print(car2.max_speed)