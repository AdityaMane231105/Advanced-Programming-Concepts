import re
from collections import Counter

def count_extensions(filenames):
    extensions = [re.search(r'\.\w+$', f).group() for f in filenames if re.search(r'\.\w+$', f)]
    return dict(Counter(extensions))

files = ["doc1.txt", "image.png", "report.pdf", "notes.txt"]
print(count_extensions(files))
