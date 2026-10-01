import re

def task1(text):
    pattern = r"ab*"
    return bool(re.fullmatch(pattern, text))

print(task1("a")) 
print(task1("abbb"))  
print(task1("ac"))