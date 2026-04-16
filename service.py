from model import Book, Library
from file_handler import save_data

# Create a single Library object to manage all books
library = Library()

def add_book():
    # Display heading
    print("\n Add Book")

    try:
        # Take inputs from user
        book_id = int(input("Enter Book ID: "))  # Convert ID to integer
        title = input("Enter Title: ").strip()   # Remove extra spaces
        author = input("Enter Author: ").strip()

        # Validate empty inputs
        if not title or not author:
            print(" Title and Author cannot be empty!")
            return

        # Check for duplicate Book ID
        for book in library.books:
            if book.book_id == book_id:
                print("Book ID already exists!")
                return

        # Create Book object and add to library
        library.add_book(Book(book_id, title, author))

        # Save updated data to file (persistence)
        save_data(library)

        print(" Book added successfully!")

    except ValueError:
        # Handle invalid numeric input
        print(" Invalid input!")


def view_books():
    # Display heading
    print("\n Book List")

    # Get all books from library
    books = library.view_books()

    # Check if library is empty
    if not books:
        print(" No books available.")
        return

    # Print each book (uses __str__ method from Book class)
    for book in books:
        print(book)


def search_book():
    # Display heading
    print("\n Search Book")

    # Take title input
    title = input("Enter title: ").strip()

    # Search books using Library method
    results = library.search_book(title)

    # Display results if found
    if results:
        for book in results:
            print(book)
    else:
        print(" Not found")


def issue_book():
    try:
        # Take Book ID input
        book_id = int(input("Enter Book ID: "))

        # Call Library method to issue book
        result = library.issue_book(book_id)

        # Handle different return cases
        if result == "success":
            save_data(library)  # Save updated status
            print(" Issued")
        elif result == "already_issued":
            print("Already issued")
        else:
            print("Not found")

    except ValueError:
        # Handle invalid input
        print("Invalid input")


def return_book():
    try:
        # Take Book ID input
        book_id = int(input("Enter Book ID: "))

        # Call Library method to return book
        result = library.return_book(book_id)

        # Handle different return cases
        if result == "success":
            save_data(library)  # Save updated status
            print("Returned")
        elif result == "already_available":
            print("Already available")
        else:
            print("Not found")

    except ValueError:
        # Handle invalid input
        print("Invalid input")