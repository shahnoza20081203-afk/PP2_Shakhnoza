import re

def task5(text):
    pattern = r"a.*b$"
    return bool(re.search(pattern, text))

print(task5("axxxb")) 
print(task5("a123_b"))  
print(task5("axxxbc"))  