from books import catalog
from books.members import details
from books.members.transactions import issue

books = catalog.list_books()
member = details.member_info()
print("Books:", books)
print("Member:", member)
print(issue.issue_book(member, books[0]))   
