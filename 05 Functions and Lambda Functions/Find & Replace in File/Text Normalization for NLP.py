import re

def normalize(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  
    contractions = {"don't": "do not", "can't": "cannot", "i'm": "i am"}
    for c, full in contractions.items():
        text = text.replace(c, full)
    return text

print(normalize("I can't believe I'm learning NLP in 2026!"))

