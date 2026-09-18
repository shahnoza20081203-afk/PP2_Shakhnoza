#1
class Animal:
    def eat(self):
        print("The animal is eating")

class Dog(Animal):
    pass

dog1 = Dog()
dog1.eat()

#2
class Vehicle:
    def start(self):
        print("The vehicle is starting")

class Car(Vehicle):
    pass

car1 = Car()
car1.start()

#3
class Person:
    def speak(self):
        print("Person is speaking")
    def walk(self):
        print("Person is walking")

class Student(Person):
    pass
student1 = Student()
student1.speak()
student1.walk()

#4
class BankAccount:
    def deposit(self):
        print("Money was deposited")

class SavingsAccount(BankAccount):
    pass
account1 = SavingsAccount()
account1.deposit()

#5
class Person:
    def introduce(self):
        print("My name is a person")
class Teacher(Person):
    pass

teacher1 = Teacher()

teacher1.introduce()