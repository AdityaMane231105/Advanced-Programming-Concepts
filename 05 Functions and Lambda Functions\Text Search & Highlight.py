import re

def search_and_highlight(text, query):
    matches = re.findall(query, text, re.IGNORECASE)
    highlighted = re.sub(query, f'**{query}**', text, flags=re.IGNORECASE)
    return len(matches), highlighted

text = "Python is great. I love python programming."
print(search_and_highlight(text, "python"))
