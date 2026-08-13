import re

def clean_html(html_content):
    return re.sub(r'<.*?>', '', html_content)

html = "<p>Hello <b>World</b></p>"
print(clean_html(html)) 

