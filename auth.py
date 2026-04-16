def signup():
    print("\nCREATE ACCOUNT")

    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()

    if not username or not password:
        print("Username/Password cannot be empty.")
        return

    role = "user"  # default role

    try:
        with open("users.txt", "r") as f:
            for line in f:
                user, _, _ = line.strip().split(",")
                if user == username:
                    print("Username already exists!")
                    return
    except:
        pass

    with open("users.txt", "a") as f:
        f.write(f"{username},{password},{role}\n")

    print("Account created successfully! Please login.\n")


def login():
    print("\nLOGIN SYSTEM")

    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()

    try:
        with open("users.txt", "r") as f:
            for line in f:
                user, pwd, role = line.strip().split(",")

                if user == username and pwd == password:
                    print("Login Successful!\n")
                    return role   # 🔥 return role

        print("User not found. Please create an account.")
        return None

    except FileNotFoundError:
        print("No users found. Please create an account first.")
        return None