import re
from datetime import datetime

def extract_dates(text):
    patterns = [
        r'\b\d{2}/\d{2}/\d{4}\b',      
        r'\b\d{2}-\d{2}-\d{4}\b',       
        r'\b\d{4}\.\d{2}\.\d{2}\b',     
        r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}, \d{4}\b'
    ]
    
    dates = []
    for pattern in patterns:
        dates.extend(re.findall(pattern, text))
    
    uniform_dates = []
    for d in dates:
        try:
            if "/" in d:
                uniform_dates.append(datetime.strptime(d, "%d/%m/%Y").strftime("%Y-%m-%d"))
            elif "-" in d:
                uniform_dates.append(datetime.strptime(d, "%m-%d-%Y").strftime("%Y-%m-%d"))
            elif "." in d:
                uniform_dates.append(datetime.strptime(d, "%Y.%m.%d").strftime("%Y-%m-%d"))
            else:
                uniform_dates.append(datetime.strptime(d, "%B %d, %Y").strftime("%Y-%m-%d"))
        except:
            pass
    return uniform_dates

text = "Dates: 12/08/2026, 08-12-2026, 2026.08.12, August 12, 2026"
print(extract_dates(text))

