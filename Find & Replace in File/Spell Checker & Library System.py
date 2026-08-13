def spell_checker(text, dictionary):
    words = text.lower().split()
    misspelled = [w.strip(".,!?") for w in words if w.strip(".,!?") not in dictionary]
    return misspelled

dictionary = {"hello", "world", "how", "are", "you", "i", "met", "dr", "smith", "today", "python", "is", "great", "love", "programming"}
text = input("Enter a block of text: ")
print("Misspelled words:", spell_checker(text, dictionary))


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is not available.")

    def return_book(self):
        self.available = True
        print(f"{self.title} has been returned.")

    def show_details(self):
        status = "Available" if self.available else "Borrowed"
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {status}")

book1 = Book("Python Basics", "John Doe", 2020)
book1.show_details()
book1.borrow()
book1.show_details()
book1.return_book()
book1.show_details()

