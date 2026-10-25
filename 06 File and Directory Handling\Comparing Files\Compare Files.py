from pathlib import Path

base_dir = Path(__file__).resolve().parent
file1_path = base_dir / "file1.txt"
file2_path = base_dir / "file2.txt"

for path in (file1_path, file2_path):
    if not path.exists():
        print(f"Missing file: {path}")
        raise SystemExit(1)

with open(file1_path, "r", encoding="utf-8") as f:
    lines1 = f.readlines()

with open(file2_path, "r", encoding="utf-8") as f:
    lines2 = f.readlines()

if lines1 == lines2:
    print("Files are identical")
else:
    print("Files are different")

    n = min(len(lines1), len(lines2))

    for i in range(n):
        if lines1[i] != lines2[i]:
            print("First different line:", i + 1)
            break
    else:
        print("First difference is after line", n)


