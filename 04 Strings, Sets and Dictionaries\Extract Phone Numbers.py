import re

def extract_phone_numbers(text):
    pattern = r'(\(\d{3}\)\s?\d{3}[-.]\d{4}|\d{3}[-.]\d{3}[-.]\d{4}|\d{10})'
    return re.findall(pattern, text)

sample_text = """
Call me at (123) 456-7890 or 987-654-3210.
You can also reach me at 123.456.7890 or 1234567890.
"""

numbers = extract_phone_numbers(sample_text)
print("Phone numbers found:", numbers)

