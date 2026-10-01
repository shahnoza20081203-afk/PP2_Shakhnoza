import re

def task8(text):
    return re.split(r"(?=[A-Z])", text)

print(task8("SplitAtUppercaseLetters")) 