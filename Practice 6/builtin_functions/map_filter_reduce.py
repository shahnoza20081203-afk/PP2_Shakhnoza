from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = list(map(lambda x: x ** 2, numbers))
print("map() - Squared:", squared)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("filter() - Evens:", evens)

total_sum = reduce(lambda x, y: x + y, numbers)
product = reduce(lambda x, y: x * y, numbers)
print("reduce() - Sum:", total_sum)
print("reduce() - Product:", product)

print(f"len: {len(numbers)}, sum: {sum(numbers)}, min: {min(numbers)}, max: {max(numbers)}")