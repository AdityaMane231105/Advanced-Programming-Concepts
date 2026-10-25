from pathlib import Path

folder = Path(__file__).resolve().parent
source = Path(input("Enter Python source file: ")).expanduser()
output = Path(input("Enter output file: ")).expanduser()

if not source.is_absolute() and not source.exists():
    source = folder / source
if not output.is_absolute():
    output = folder / output

try:
    with source.open("r", encoding="utf-8-sig") as file:
        lines = file.readlines()

    with output.open("w", encoding="utf-8") as file:
        for line in lines:
            if not line.lstrip().startswith("#"):
                file.write(line)

    print("Comments removed. Output saved to:", output)
except FileNotFoundError:
    print("Source file not found:", source) 
    
    
