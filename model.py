class Book:
    def __init__(self, book_id, title, author, available=True):
        # Initialize book details
        # Convert book_id to integer for consistent comparison
        self.book_id = int(book_id)
        self.title = title
        self.author = author
        self.available = available  # True = available, False = issued

    def __str__(self):
        # Convert object to readable string format for display
        status = "Available" if self.available else "Not Available"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        # Initialize empty list to store all book objects
        self.books = []

    def add_book(self, book):
        # Add a new Book object to the library list
        self.books.append(book)

    def view_books(self):
        # Return all books in the library
        return self.books

    def search_book(self, title):
        # Search books by title (case-insensitive)
        # Returns list of matching books
        return [book for book in self.books if title.lower() in book.title.lower()]

    # 🔥 FIXED ISSUE BOOK
    def issue_book(self, book_id):
        # Loop through all books to find matching ID
        for book in self.books:
            if book.book_id == book_id:
                # If book is already issued (not available)
                if not book.available:
                    return "already_issued"
                # Mark book as issued (not available)
                book.available = False
                return "success"
        # If no book found with given ID
        return "not_found"

    # 🔥 FIXED RETURN BOOK
    def return_book(self, book_id):
        # Loop through all books to find matching ID
        for book in self.books:
            if book.book_id == book_id:
                # If book is already available (not issued)
                if book.available:
                    return "already_available"
                # Mark book as returned (available again)
                book.available = True
                return "success"
        # If no book found with given ID
        return "not_found"