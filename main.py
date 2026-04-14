from service import *                     # Import all CRUD functions and shared library object
from file_handler import load_data, save_data   # Import file handling functions
from auth import login, signup           # Import authentication functions


def auth_menu():
    # Display authentication options
    print("\nAUTH MENU")
    print("1. Login")
    print("2. Create Account")
    print("3. Exit")


def menu():
    # Display main system menu
    print("\n LIBRARY MANAGEMENT SYSTEM")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")


def main():

    # AUTHENTICATION LOOP
    # Keeps asking until user logs in successfully or exits
    while True:
        auth_menu()
        choice = input("Enter choice: ")

        if choice == '1':
            # Attempt login
            if login():
                break   # Exit loop only if login successful
        elif choice == '2':
            # Create new user account
            signup()
        elif choice == '3':
            # Exit program completely
            print("Exiting...")
            return
        else:
            # Handle invalid input
            print("Invalid choice")

    # Load book data from file after successful login
    load_data(library)

    # MAIN MENU LOOP
    # Runs continuously until user chooses exit
    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == '1':
            add_book()        # Create (Add new book)
        elif choice == '2':
            view_books()      # Read (Display all books)
        elif choice == '3':
            search_book()     # Read (Search books by title)
        elif choice == '4':
            issue_book()      # Update (Mark book as issued)
        elif choice == '5':
            return_book()     # Update (Mark book as returned)
        elif choice == '6':
            # Save all data before exiting
            save_data(library)
            print(" Data saved. Exiting...")
            break
        else:
            # Handle invalid menu choice
            print(" Invalid choice")


# Entry point of the program
if __name__ == "__main__":
    main()