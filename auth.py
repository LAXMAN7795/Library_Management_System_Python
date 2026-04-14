def signup():
    # Display signup heading
    print("\nCREATE ACCOUNT")

    # Take username and password input from user
    # strip() removes extra spaces from beginning and end
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()

    # Validate that fields are not empty
    if not username or not password:
        print("Username/Password cannot be empty.")
        return

    # Check if user already exists in file
    try:
        with open("users.txt", "r") as f:
            for line in f:
                # Split stored data into username and password
                user, _ = line.strip().split(",")
                # If entered username matches existing one
                if user == username:
                    print("Username already exists!")
                    return
    except FileNotFoundError:
        # If file does not exist, ignore and continue (new user case)
        pass

    # Save new user credentials into file
    with open("users.txt", "a") as f:
        # Store in "username,password" format
        f.write(f"{username},{password}\n")

    # Success message
    print("Account created successfully! Please login.\n")


def login():
    # Display login heading
    print("\nLOGIN SYSTEM")

    # Take username and password input
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()

    try:
        with open("users.txt", "r") as f:
            for line in f:
                # Split stored credentials
                user, pwd = line.strip().split(",")
                # Check if both username and password match
                if user == username and pwd == password:
                    print("Login Successful!\n")
                    return True

        # If no matching user found
        print("User not found. Please create an account before logging in.")
        return False

    except FileNotFoundError:
        # If file does not exist (no users created yet)
        print("No users found. Please create an account first.")
        return False