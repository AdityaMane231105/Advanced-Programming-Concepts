books = []

def add_book():
    book_id = input("Book ID: ")
    title = input("Title: ")
    author = input("Author: ")
    books.append([book_id, title, author, "Available"])

def search_book():
    book_id = input("Enter Book ID: ")
    for book in books:
        if book[0] == book_id:
            print(book)
            return
    print("Book not found")

def issue_book():
    book_id = input("Enter Book ID: ")
    for book in books:
        if book[0] == book_id:
            if book[3] == "Available":
                book[3] = "Issued"
                print("Book issued")
            else:
                print("Book is already issued")
            return
    print("Book not found")

def return_book():
    book_id = input("Enter Book ID: ")
    for book in books:
        if book[0] == book_id:
            book[3] = "Available"
            print("Book returned")
            return
    print("Book not found")

def display_available():
    for book in books:
        if book[3] == "Available":
            print(book)

while True:
    print("1 Add  2 Search  3 Issue  4 Return  5 Available  6 Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        display_available()
    elif choice == "6":
        break
    else:
        print("Invalid choice")

