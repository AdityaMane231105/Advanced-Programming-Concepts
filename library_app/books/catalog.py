def list_books():
    return ["Python Basics","Data Science","AI Fundamentals"]

def get_book_details(title):
    books = {
        "Python Basics": {"author": "John Doe", "year": 2020},
        "Data Science": {"author": "Jane Smith", "year": 2019},
        "AI Fundamentals": {"author": "Bob Johnson", "year": 2021}
    }
    return books.get(title, {"author": "Unknown", "year": 0})       

