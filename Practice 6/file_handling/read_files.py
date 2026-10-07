import os

filename = "sample.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write("Line 1: Python File Handling\nLine 2: Built-in Functions\nLine 3: End of file\n")

print("--- read() ---")
with open(filename, "r", encoding="utf-8") as f:
    print(f.read())

print("--- readline() ---")
with open(filename, "r", encoding="utf-8") as f:
    print(f.readline().strip())
    print(f.readline().strip())

print("--- readlines() ---")
with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(lines)

line_count = len(lines)
print(f"\nTotal lines in '{filename}': {line_count}")

if os.path.exists(filename):
    os.remove(filename)