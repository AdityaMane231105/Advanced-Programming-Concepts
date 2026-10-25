import shutil
import sys

print("Python version:", sys.version.split()[0])
print("Python executable:", sys.executable)
print("Python implementation:", sys.implementation.name)
print("pip command:", shutil.which("pip") or "Not found on PATH")
