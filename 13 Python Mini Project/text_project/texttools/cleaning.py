import string
def clean(text):
    return ' '.join(text.translate(str.maketrans('','',string.punctuation)).split())    
