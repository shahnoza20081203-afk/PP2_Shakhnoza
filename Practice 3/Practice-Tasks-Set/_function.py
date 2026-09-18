#1
def grams_to_ounces(grams):
    return 28.3495231 * grams

grams = 50
ounces = grams_to_ounces(grams)
print(f"{grams} grams = {ounces} ounces")

#2
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

f_temp = 55.4
c_temp = fahrenheit_to_celsius(f_temp)
print(f"{f_temp}°F = {c_temp:.2f}°C")

#3
def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if (chickens * 2 + rabbits * 4) == numlegs:
            return chickens, rabbits
    return None, None

heads = 35
legs = 94
chickens, rabbits = solve(heads, legs)
print(f"Chickens: {chickens}")
print(f"Rabbits: {rabbits}")

#4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 20]
print(f"Original list: {nums}")
print(f"Prime numbers: {filter_prime(nums)}")

#5
import itertools

def print_permutations(user_string):
    perms = [''.join(p) for p in itertools.permutations(user_string)]
    for p in perms:
        print(p)

word = "tr"
print(f"Permutations of '{word}':")
print_permutations(word)

#6
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

text = "We are ready"
reversed_text = reverse_words(text)
print(f"Original: {text}")
print(f"Reversed: {reversed_text}")

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

print(has_33([1, 3, 3]))     
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3]))    

#8
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
print(spy_game([1, 0, 2, 4, 0, 5, 7])) 
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  

#9
import math

def sphere_volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)

r = 3
volume = sphere_volume(r)
print(f"Volume of sphere with radius {r}: {volume:.2f}")

#10
def unique_elements(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

original_list = [1, 2, 2, 3, 4, 4, 4, 5]
print(f"Original list: {original_list}")
print(f"Unique list: {unique_elements(original_list)}")

#11
def is_palindrome(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

print(is_palindrome("radar"))   
print(is_palindrome("hello"))             

#12
def histogram(lst):
    for num in lst:
        print('*' * num)

histogram([4, 9, 7])

#13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
guess_the_number()


