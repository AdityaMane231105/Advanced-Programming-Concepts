def remove_stopwords(text):
    stopwords = {"is", "and", "the", "a", "an", "in", "on", "at", "to"}
    words = text.split()
    cleaned = [w for w in words if w.lower() not in stopwords]
    return " ".join(cleaned)

print(remove_stopwords("This is the best example in the text"))
