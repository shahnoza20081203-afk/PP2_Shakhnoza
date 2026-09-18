students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

products = [
    ("Phone", 300000),
    ("Laptop", 500000),
    ("Headphones", 50000)
]
result = sorted(products, key=lambda product: product[1])
print(result)

numbers = [5, 2, 8, 1, 3]
result = sorted(numbers, key=lambda x: x, reverse=True)
print(result)

words = ["apple", "cat", "banana", "dog"]
result = sorted(words, key=lambda word: len(word))
print(result)