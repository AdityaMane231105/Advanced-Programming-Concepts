import re

def extract_hashtags(text):
    return re.findall(r'#\w+', text)

post = "Loving the vibes! #summer #2026 #fun_time"
print(extract_hashtags(post))

