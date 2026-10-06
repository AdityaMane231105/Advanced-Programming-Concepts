import string
 
def clean(text):
    for ch in string.punctuation:
        text = text.replace(ch, "")
    return " ".join(text.split())
