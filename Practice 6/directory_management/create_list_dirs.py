import os

target_path = "."

nested_dir = "nested/level1/level2"
os.makedirs(nested_dir, exist_ok=True)
print(f"Created nested directory: {nested_dir}")

all_entries = os.listdir(target_path)
only_files = [f for f in all_entries if os.path.isfile(os.path.join(target_path, f))]
only_dirs = [d for d in all_entries if os.path.isdir(os.path.join(target_path, d))]

print("\n--- Only Directories ---")
print(only_dirs)

print("\n--- Only Files ---")
print(only_files)

print("\n--- All Directories and Files ---")
print(all_entries)

py_files = [f for f in os.listdir(".") if f.endswith(".py")]
print("\n--- Python Files (.py) ---")
print(py_files)

os.removedirs(nested_dir)