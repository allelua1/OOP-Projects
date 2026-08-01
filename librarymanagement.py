class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)

    def add_user(self, user):
        self.users.append(user)

    def borrow_book(self, book_isbn, user_id):
        book = next((book for book in self.books if book.isbn == book_isbn), None)
        user = next((user for user in self.users if user.id == user_id), None)

        if not book:
            return "Book not found."
        if not user:
            return "User not found."
        if not book.available:
            return "Book is not available."
        # update book and user
        book.available = False
        book.borrower = user
        user.borrowed_books.append(book)

        return "Book borrowed successfully."

    def return_book(self, book_isbn, user_id):
        book = next((book for book in self.books if book.isbn == book_isbn), None)
        user = next((user for user in self.users if user.id == user_id), None)

        # checking if book and user exist and book was borrowed by this user
        if not book:
            return "Book not found."
        if not user:
            return "User not found."
        if book.available or book.borrower != user:
            return "This book was not borrowed by this user."

        # update book and user
        book.available = True
        book.borrower = None
        user.borrowed_books.remove(book)

        return "Book returned successfully."


    def __str__(self):
        # return f"Library Name: {self.name}, The number of books: {len(self.books)}, The number of users: {len(self.users)}"
        return f"{self.name} Library with {self.books} books and {len(self.users)} users."

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.borrower = None
    def __str__(self):
        if self.available:
            return f"{self.title} by {self.author} (ISBN: {self.isbn} - Available)"
        return f"{self.title} by {self.author} (ISBN: {self.isbn} - Not Available"

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.id = user_id
        self.borrowed_books = []
    def __str__(self):
        return f"User: {self.name} (ID: {self.id}) - Borrowed Books: {len(self.borrowed_books)}"
    def return_all_books(self, library):
                # TODO: Create a copy of self.books_borrowed to iterate over (use books_to_return = self.books_borrowed.copy())
        # TODO: Initialize a counter variable (return_count) to track the number of books returned
        # TODO: For each book in the copy:
        #       - Set book.available to True
        #       - Set book.borrower to None
        #       - Remove the book from self.books_borrowed
        #       - Increment the return_count
        # TODO: Return the return_count (number of books returned)
        books_to_return = self.borrowed_books.copy()
        return_count = 0
        for book in books_to_return:
            book.available = True
            book.borrower = None
            self.borrowed_books.remove(book)
            return_count += 1
        return return_count

print("Library Management System")
print("\n Create user:\n")

user_id = "1"
name = "John Doe"
user = User(name, user_id)
print(user)
print(f"Borrowed Books: {len(user.borrowed_books)}\n")

# Borrow ad return all
library = Library("Community Library")
# add books and useers
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", "123456"))
library.add_book(Book("To Kill a Mockingbird", "Harper Lee", "789012"))
library.add_book(Book("1984", "George Orwell", "345678"))

user = User("Alice", "U001")
library.add_user(user)

# borrow books
library.borrow_book("123456", "U001")
library.borrow_book("789012", "U001")
library.borrow_book("345678", "U001")

print(f"Books borrowed before: {len(user.borrowed_books)}")

# Return all books
num_returned = user.return_all_books(library)

print(f"Books returned: {num_returned}")
print(f"Books borrowed after: {len(user.borrowed_books)}")

# check if all books are available
for book in library.books:
    print(f"Book {book.isbn} available: {book.available}")
    


    
    