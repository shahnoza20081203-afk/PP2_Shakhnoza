fruits = ["apple", "banana", "cherry", "date"]
print("--- enumerate() ---")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
cities = ["Almaty", "Astana", "Shymkent"]

print("\n--- zip() ---")
for name, score, city in zip(names, scores, cities):
    print(f"{name} (Score: {score}) from {city}")

val = "123"
print("\n--- Type Conversions & Verification ---")
print("type:", type(val))
print("isinstance int:", isinstance(val, int))

num = int(val)
print("Converted to int:", num, type(num))

float_list = [3.14, 1.41, 2.71]
print("sorted():", sorted(float_list))