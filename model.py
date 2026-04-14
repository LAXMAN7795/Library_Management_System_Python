# model.py

class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    # Add a new book
    def add_book(self, book):
        self.books.append(book)

    # View all books
    def view_books(self):
        return self.books

    # Search book by title
    def search_book(self, title):
        result = []
        for book in self.books:
            if title.lower() in book.title.lower():
                result.append(book)
        return result

    # Issue a book
    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and book.available:
                book.available = False
                return True
        return False

    # Return a book
    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and not book.available:
                book.available = True
                return True
        return False