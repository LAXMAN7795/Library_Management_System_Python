from service import *
from file_handler import load_data, save_data
from auth import login, signup


def auth_menu():
    print("\nAUTH MENU")
    print("1. Login")
    print("2. Create Account")
    print("3. Exit")


def admin_menu():
    print("\nADMIN MENU")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")


def user_menu():
    print("\nUSER MENU")
    print("1. View Books")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")


def main():

    role = None

    # AUTH LOOP
    while True:
        auth_menu()
        choice = input("Enter choice: ")

        if choice == '1':
            role = login()
            if role:
                break
        elif choice == '2':
            signup()
        elif choice == '3':
            return
        else:
            print("Invalid choice")

    # Load data after login
    load_data(library)

    # ROLE-BASED ACCESS
    if role == "admin":
        while True:
            admin_menu()
            choice = input("Enter choice: ")

            if choice == '1':
                add_book()
            elif choice == '2':
                view_books()
            elif choice == '3':
                search_book()
            elif choice == '4':
                save_data(library)
                print("Exiting...")
                break
            else:
                print("Invalid choice")

    elif role == "user":
        while True:
            user_menu()
            choice = input("Enter choice: ")

            if choice == '1':
                view_books()
            elif choice == '2':
                search_book()
            elif choice == '3':
                issue_book()
            elif choice == '4':
                return_book()
            elif choice == '5':
                save_data(library)
                print("Exiting...")
                break
            else:
                print("Invalid choice")


if __name__ == "__main__":
    main()