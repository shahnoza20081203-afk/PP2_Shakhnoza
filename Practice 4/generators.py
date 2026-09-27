#1
def squares_numbers(n):
    for i in range(n+1):
        yield i**2

for square in squares_numbers(3):
    print(square)

#2
def even_numbers(n):
    for i in range(n+1):
        if i%2==0:
            yield str(i)

n=int(input("Enter n: "))
print(",".join(even_numbers(n)))

#3
def divisible_by_3_4(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i
    
for number in divisible_by_3_4(30):
    print(number)

#4
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a = 2
b = 4
for sq in squares(a, b):
    print(sq)

#5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

for num in countdown(4):
    print(num)
