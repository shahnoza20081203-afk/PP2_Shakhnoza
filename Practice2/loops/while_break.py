i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i= 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1

numbers = [2, 4, 6, 8, 10]
i = 0
while i < len(numbers):
    if numbers[i] == 6:
        print("Found!")
        break
    i += 1

i = 1
while True:
    print(i)
    if i > 10:
        break
    i += 1

count = 10
while count > 0:
    print(count)
    if count == 5:
        break
    count -= 1