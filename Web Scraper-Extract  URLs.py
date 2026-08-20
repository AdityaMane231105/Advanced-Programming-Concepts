import re

def extract_urls(text):
    pattern = r'(https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[^\s"<]*)|(www\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[^\s"<]*)'
    urls = re.findall(pattern, text)
    return [url for tup in urls for url in tup if url]

paragraphs = """
I was reading an article yesterday and found a useful resource at https://docs.python.org/3/tutorial/.
You can also check out www.learnprogramming.com for beginner-friendly guides.

Later, I visited https://github.com to explore open-source projects.
Another great site is www.stackoverflow.com where developers ask and answer coding questions.

For UI/UX design inspiration, I often browse https://dribbble.com and www.behance.net.
"""

print(extract_urls(paragraphs))

