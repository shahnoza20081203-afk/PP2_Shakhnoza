import re

def task7(text):
    return re.sub(r"_([a-z])", lambda m: m.group(1).upper(), text)

print(task7("hello_world_test"))  