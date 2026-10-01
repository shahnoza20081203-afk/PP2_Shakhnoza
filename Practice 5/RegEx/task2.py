import re

def task2(text):
    pattern = r"ab{2,3}"
    return bool(re.fullmatch(pattern, text))

print(task2("abb"))  
print(task2("abbb"))  
print(task2("ab"))  