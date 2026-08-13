import re

def extract_urls(html_content):
    pattern = r'(https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[^\s"<]*)|(www\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[^\s"<]*)'
    urls = re.findall(pattern, html_content)
    return [url for tup in urls for url in tup if url]

html = '<a href="https://example.com">Link</a> Visit www.test.org now!'
print(extract_urls(html))

