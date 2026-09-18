numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

numbers = [-5, 3, -2, 8, 0, 10]
result = filter(lambda x: x > 0, numbers)
print(list(result))

words = ["apple", "cat", "banana", "dog", "orange"]
result = filter(lambda word: len(word) > 5, words)
print(list(result))

numbers = [5, 12, 8, 20, 15]
result = filter(lambda x: x > 10, numbers)
print(list(result))

ages = [16, 19, 17, 21, 18, 20]
result = filter(lambda age: age > 18, ages)
print(list(result))