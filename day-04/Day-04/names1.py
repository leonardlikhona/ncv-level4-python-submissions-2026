from pathlib import Path

file_path = Path("names.txt")

initial_names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
with file_path.open("w", encoding="utf-8") as f:
    for name in initial_names:
        f.write(f"{name}\n")

print("--- Names in uppercase ---")
with file_path.open("r", encoding="utf-8") as f:
    for line in f:
        cleaned = line.strip().upper()
        print(cleaned)

with file_path.open("a", encoding="utf-8") as f:
    f.write("Fiona\n")

with file_path.open("r", encoding="utf-8") as f:
    line_count = sum(1 for _ in f)

print(f"\nTotal lines after appending: {line_count}")

missing_file = Path("does_not_exist.txt")
try:
    with missing_file.open("r", encoding="utf-8") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print(f"\nCould not read '{missing_file}': file does not exist.")