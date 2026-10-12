names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

print("Итерация с enumerate():")
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")

print("\nПараллельная итерация с zip():")
for name, score in zip(names, scores):
    print(f"Студент {name} получил {score} баллов.")