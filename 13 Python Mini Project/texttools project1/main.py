from texttools.cleaning import clean
from texttools.tokenization import tokenize
from texttools.frequency import frequency
 
text = input("Enter text: ")
text = clean(text)
 
print("Clean text:", text)
print("Tokens:", tokenize(text))
print("Frequency:", frequency(text))
