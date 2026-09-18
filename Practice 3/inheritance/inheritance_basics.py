#1
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
x = Person("John", "Doe")
x.printname()

#2
class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()

#3
class Animal:
    def eat(self):
        print("The animal is eating")

class Dog(Animal):
    pass

dog1 = Dog()
dog1.eat()

#4
class Animal:
    def eat(self):
        print("The animal is eating")
class Dog(Animal):
    def bark(self):
        print("Woof!")
dog1 = Dog()
dog1.eat()
dog1.bark()

#5