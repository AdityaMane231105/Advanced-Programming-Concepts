from texttools import cleaning,tokenization,frequency
t="Hello, world!! Hello   Copilot."
c=cleaning.clean(t)
tok=tokenization.tokenize(c)
print(frequency.word_freq(tok))
