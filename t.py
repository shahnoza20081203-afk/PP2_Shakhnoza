import os
with open("values.txt", "w") as f:
    f.write("10 \n 3.5 \n 7 \n hello")
with open("values.txt", "r") as f:
    a=f.read()
print(a)
with open("values.txt", "a") as f:
    f.write("42")
