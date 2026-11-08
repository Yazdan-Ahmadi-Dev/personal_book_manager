from books import show_books, save_books, load_books
from dotenv import load_dotenv
import os


load_dotenv()


name = input("Hello, enter your name: ")
print("Welcome", name)
print( )


admin_mode = input("Do you want to enter admon mode (yes/no)?  ")

if admin_mode == "yes":
    admin_password = input("Enter admin password:  ")
    if admin_password == os.getenv("admin_password"):
        print("Admin mode is activated")
    else:
        print("Wrong password")

print( )




books = load_books()
count = int(input("How many book do you want to add? "))
for i in range(count):
    book_name = input ("Enter the book name: ")
    priority = input("enter priority(low/medium/high) :").lower()
    book = {
        "name": book_name,
        "priority" : priority
    }
    books.append(book)


show_books(books)
save_books(books)
load_books()

