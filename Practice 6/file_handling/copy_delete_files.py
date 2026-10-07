import os
import shutil

source = "source.txt"
destination = "backup_source.txt"

with open(source, "w", encoding="utf-8") as f:
    f.write("Important data to copy and delete.\n")

shutil.copy(source, destination)
print(f"Copied '{source}' to '{destination}'")

def check_and_delete(path):
    print(f"\n--- Checking path: {path} ---")
    
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return

    dirname, filename = os.path.split(path)
    print(f"Directory portion: '{dirname}'")
    print(f"Filename portion: '{filename}'")

    print(f"Readable: {os.access(path, os.R_OK)}")
    print(f"Writable: {os.access(path, os.W_OK)}")
    print(f"Executable: {os.access(path, os.X_OK)}")

    if os.access(path, os.W_OK):
        os.remove(path)
        print(f"File '{path}' deleted successfully.")

check_and_delete(source)
check_and_delete(destination)