from functools import reduce

numbers = [1, 2, 3, 4, 5]

total_sum = reduce(lambda x, y: x + y, numbers)

product = reduce(lambda x, y: x * y, numbers)

print("Сумма элементов (reduce):", total_sum)
print("Произведение элементов (reduce):", product)