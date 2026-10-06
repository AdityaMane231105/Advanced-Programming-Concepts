from pathlib import Path

base_dir = Path(__file__).resolve().parent

with open(base_dir / "file1.txt", "r") as f:
    text1 = f.read()

with open(base_dir / "file2.txt", "r") as f:
    text2 = f.read()

with open(base_dir / "file3.txt", "w") as f:
    f.write(text1)
    f.write("\n")
    f.write(text2)

print("Third file created")

