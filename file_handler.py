from model import Book   # Import Book class to create objects while loading data

def load_data(library):
    # Load book data from file into the library object
    try:
        # Open file in read mode
        with open("data.txt", "r") as f:
            for line in f:
                line = line.strip()   # Remove spaces/newlines

                # Skip empty lines
                if not line:
                    continue

                parts = line.split(",")

                # Skip invalid/corrupt lines
                if len(parts) != 4:
                    continue

                # Split each line into components
                book_id, title, author, available = parts

                # Create Book object
                # Convert book_id to int and available to boolean
                book = Book(int(book_id), title, author, available == "True")

                # Add book to library collection
                library.add_book(book)

    except FileNotFoundError:
        # If file does not exist, ignore (start with empty library)
        pass


def save_data(library):
    # Save all books from library object into file
    # Open file in write mode (overwrites old data)
    with open("data.txt", "w") as f:
        for book in library.books:
            # Write book details in CSV format
            # Format: id,title,author,available
            f.write(f"{book.book_id},{book.title},{book.author},{book.available}\n")