import re


def task7(snake_str):
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])

print(task7("snake_case_string"))  