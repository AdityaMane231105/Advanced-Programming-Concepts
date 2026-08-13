import re

def split_sentences(text):
    sentences = re.split(r'(?<!Dr)(?<!Mr)(?<!Mrs)(?<!Ms)(?<=[.!?])\s+', text)
    return sentences

text = "Hello world! How are you? I met Dr. Smith today."
print(split_sentences(text))
