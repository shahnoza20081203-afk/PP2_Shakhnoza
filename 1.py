#1
amount=float(input("Enter: "))
if amount>5000:
    percent=20
elif amount>1000:
    percent=10
else:
    percent=0
with_percent=amount*(percent/100)
final=amount-with_percent
print(final)

#2
text="Add a dda"
clear=text.lower().replace(" ", "")
palindrome=clear==clear[::-1]
print(palindrome)

#3
numbers = [10, 20, 5, 20, 30, 10, 50, 5, 100]
number=list(set(numbers))
filter=[]
for num in number:
    if num>15:
        filter.append(num)
filter.sort()
print(filter)

#4
text = "python is great and python is easy to learn"
words=text.split()
count={}
for word in words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(count)

#5
def safe_fetch(dictionary, key, default=None):
    if key in dictionary:
        return dictionary[key]
    else:
        return default
user={"name": "Анна", "age": 20}

print(safe_fetch(user, "name", "Неизвестно"))      # Выведет: Анна (ключ есть)
print(safe_fetch(user, "city", "Город не указан"))  # Выведет: Город не указан (ключа нет, вернулся default)
print(safe_fetch(user, "city"))