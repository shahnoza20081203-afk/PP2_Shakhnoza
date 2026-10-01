import re

def task4(text):
    pattern = r"[A-Z][a-z]+"
    return re.findall(pattern, text)

print(task4("Hello World python RegEx"))