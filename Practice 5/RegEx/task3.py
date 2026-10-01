import re

def task3(text):
    pattern = r"[a-z]+_[a-z]+"
    return re.findall(pattern, text)

print(task3("hello_world test_var Variable_Name_test"))
