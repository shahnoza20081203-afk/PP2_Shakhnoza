fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)

word = "banana"
for letter in word:
    if letter == "a":
        continue
    print(letter)

numbers = [2, -1, 5, -3, 7]
for number in numbers:
    if number < 0:
        continue
    print(number)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)