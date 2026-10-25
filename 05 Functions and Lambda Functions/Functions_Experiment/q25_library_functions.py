books = {
    "The Hobbit": {"author": "J. R. R. Tolkien", "available": True},
    "Matilda": {"author": "Roald Dahl", "available": True},
    "Dune": {"author": "Frank Herbert", "available": False}
}


def add_book(title, author):
    books[title] = {"author": author, "available": True}


def issue_book(title):
    if title not in books or not books[title]["available"]:
        return False
    books[title]["available"] = False
    return True


def return_book(title):
    if title not in books or books[title]["available"]:
        return False
    books[title]["available"] = True
    return True


def search_books(query):
    query = query.lower()
    return {title: details for title, details in books.items() if query in title.lower() or query in details["author"].lower()}


def available_books():
    return [title for title, details in books.items() if details["available"]]


add_book("Pride and Prejudice", "Jane Austen")
print("Issued:", issue_book("The Hobbit"))
print("Search:", search_books("dahl"))
print("Available:", available_books())
