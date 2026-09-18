numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

numbers = [2, 3, 4, 5]
result = map(lambda x: x ** 2, numbers)
print(list(result))

numbers = [5, 10, 15, 20]
result = map(lambda x: x + 10, numbers)
print(list(result))

words = ["apple", "banana", "cherry"]
result = map(lambda word: word.upper(), words)
print(list(result))

words = ["cat", "apple", "banana"]
result = map(lambda word: len(word), words)
print(list(result))