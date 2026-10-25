text = "Hello World!"

def char_frequency(text, case_sensitive=False):
    if not case_sensitive:
        text = text.lower()
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

print(char_frequency(text))

