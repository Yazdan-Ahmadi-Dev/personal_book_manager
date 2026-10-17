from books import show_books



name = input("Hello, enter your name: ")
print("Welcome", name)
print( )


books = []
count = int(input("How many book do you want to add? "))
for i in range(count):
    book= input ("Enter the book name: ")
    books.append(book)


show_books(books)

