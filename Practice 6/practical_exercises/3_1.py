numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = list(map(lambda x: x ** 2, numbers))
print("Квадраты чисел (map):", squares)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Четные числа (filter):", evens)