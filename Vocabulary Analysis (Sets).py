book1 = {"python", "code", "program", "data"}
book2 = {"java", "code", "program", "design"}

print("Unique words in book1:", book1)
print("Unique words in book2:", book2)
print("Common words:", book1 & book2)
print("Unique to book1:", book1 - book2)
print("Unique to book2:", book2 - book1)
print("Total unique words:", book1 | book2)
