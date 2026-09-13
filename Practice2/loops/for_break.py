fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

numbers = [5, 8, 3, -2, 7]
for number in numbers:
    if number < 0:
        break
    print(number)

total = 0
for number in range(1, 10):
    total += number
    if total > 10:
        break
print(total)