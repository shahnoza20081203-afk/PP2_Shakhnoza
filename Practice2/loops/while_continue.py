i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue
    print(i)

numbers = [3, -2, 5, -1, 8]
i = 0
while i < len(numbers):
    number = numbers[i]
    i += 1
    if number < 0:
        continue
    print(number)

text = "Hello World"
i = 0
while i < len(text):
    letter = text[i]
    i += 1
    if letter == " ":
        continue
    print(letter)

i = 0
while i < 10:
    i += 1
    if i > 5:
        continue
    print(i)
