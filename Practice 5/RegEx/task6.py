import re

def task6(text):
    pattern = r"[ ,\.]"
    return re.sub(pattern, ":", text)

print(task6("Hello, world. How are you")) 