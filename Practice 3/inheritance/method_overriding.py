#1
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog says Woof")

animal1 = Animal()
dog1 = Dog()

animal1.sound()
dog1.sound()

#2
class Vehicle:
    def move(self):
        print("The vehicle is moving")
class Car(Vehicle):
    def move(self):
        print("The car is driving")

car1 = Car()
car1.move()

#3
class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

circle1 = Circle()
circle1.draw()

#4
class Device:
    def start(self):
        print("The device is starting")

class Phone(Device):
    def start(self):
        print("The phone is turning on")

phone1 = Phone()
phone1.start()