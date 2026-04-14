from model import Book, Library

# Create a single library object
library = Library()


# 🔹 Add Book (CREATE)
def add_book():
    print("\n Add Book")

    try:
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ").strip()
        author = input("Enter Author Name: ").strip()

        # Validation
        if not title or not author:
            print(" Title and Author cannot be empty!")
            return

        # Check duplicate ID
        for book in library.books:
            if book.book_id == book_id:
                print(" Book ID already exists!")
                return

        new_book = Book(book_id, title, author)
        library.add_book(new_book)

        print(" Book added successfully!")

    except ValueError:
        print(" Invalid input! Book ID must be a number.")


# 🔹 View Books (READ)
def view_books():
    print("\n List of Books")

    books = library.view_books()

    if not books:
        print("No books available.")
        return

    for book in books:
        print(book)   # uses __str__ method from model


# 🔹 Search Book (READ)
def search_book():
    print("\n Search Book")

    title = input("Enter book title: ").strip()

    if not title:
        print(" Search cannot be empty!")
        return

    results = library.search_book(title)

    if results:
        print("\n Matching Books:")
        for book in results:
            print(book)
    else:
        print(" No matching books found.")


# 🔹 Issue Book (UPDATE)
def issue_book():
    print("\n Issue Book")

    try:
        book_id = int(input("Enter Book ID to issue: "))

        if library.issue_book(book_id):
            print(" Book issued successfully!")
        else:
            print(" Book not found or already issued.")

    except ValueError:
        print(" Invalid input! Please enter a number.")


# 🔹 Return Book (UPDATE)
def return_book():
    print("\n Return Book")

    try:
        book_id = int(input("Enter Book ID to return: "))

        if library.return_book(book_id):
            print(" Book returned successfully!")
        else:
            print(" Book not found or already available.")

    except ValueError:
        print(" Invalid input! Please enter a number.")