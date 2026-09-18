def word_freq(tokens):
    return {w:tokens.count(w) for w in set(tokens)}
