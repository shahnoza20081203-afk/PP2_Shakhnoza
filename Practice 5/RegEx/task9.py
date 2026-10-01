import re

def task9(text):
    return re.sub(r"(?<=[a-z])(?=[A-Z])", " ", text)

print(task9("InsertSpacesBetweenWords"))  