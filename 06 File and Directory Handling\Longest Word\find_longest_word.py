from pathlib import Path

file_path = Path(__file__).resolve().parent / "student.txt"

if file_path.exists():
    with file_path.open("r", encoding="utf-8") as f:
        words = f.read().split()

    if words:
        longest = max(words, key=len)
        print("Longest word:", longest)
    else:
        print("File is empty")
else:
    print("student.txt not found in the same folder as this script.")
