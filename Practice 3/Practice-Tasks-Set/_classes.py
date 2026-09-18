import math
#1
class StringProcessor:
    def __init__(self):
        self.user_string = ""

    def getString(self):
        self.user_string = input("Enter the string: ")

    def printString(self):
        print(self.user_string.upper())

processor = StringProcessor()
processor.getString()
processor.printString()

#2
class Shape:
    def area(self):
        print(0)

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length ** 2)

shape = Shape()
shape.area()  
square = Square(5)
square.area()

#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(self.length * self.width)

rectangle = Rectangle(4, 6)
rectangle.area()

#4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates of a point: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
p1 = Point(3, 4)
p1.show()

#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdrawal denied! Requested: ${amount}, Available: ${self.balance}")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew: ${amount}. Remaining balance: ${self.balance}")

account = Account("Don", 100)
account.deposit(50)     
account.withdraw(30)    
account.withdraw(170)  

#6
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(math.isqrt(n)) + 1))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(is_prime, numbers))

print(f"Original list: {numbers}")
print(f"Prime numbers: {prime_numbers}")