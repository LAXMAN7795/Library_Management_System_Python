# 📚 Library Management System (Console-Based Python Project)

## 📌 Project Overview

The **Library Management System** is a menu-driven console application developed using Python.
It allows users to manage books efficiently by performing operations like adding, viewing, searching, issuing, and returning books.

The system is enhanced with:

* 🔐 User Authentication (Login & Signup)
* 🧑‍💼 Role-Based Access Control (Admin & User)
* 💾 File Handling for data persistence
* 🧠 Object-Oriented Programming (OOP)
* ⚠️ Exception Handling and Input Validation

---

## 🚀 Features

### 📖 Book Management

* Add new books *(Admin only)*
* View all books
* Search books by title
* Issue books *(User only)*
* Return books *(User only)*

---

### 🔐 Authentication & Authorization

* User Signup (stored in `users.txt`)
* User Login validation
* Role-Based Access:

  * **Admin** → Manage books
  * **User** → Borrow/return books

---

### 💾 File Handling

* Book data stored in `data.txt`
* User credentials stored in `users.txt`
* Persistent storage across multiple runs

---

### ⚙️ Error Handling

* Handles invalid inputs
* Prevents duplicate book IDs
* Prevents duplicate usernames
* Skips corrupted or empty file data

---

## 🧱 Project Structure

```bash id="proj_struct"
Library_management_system/
│
├── main.py            # Entry point (menu + role-based flow)
├── model.py           # Classes (Book, Library)
├── service.py         # CRUD operations (business logic)
├── file_handler.py    # File operations (load/save data)
├── auth.py            # Login & Signup system
├── data.txt           # Book storage
├── users.txt          # User credentials with roles
```

---

## 🧠 Technologies Used

* Python (Core Python)
* File Handling (`.txt`)
* Object-Oriented Programming (OOP)
* Exception Handling
* Role-Based Access Control (RBAC)

---

## 🔄 Workflow

```text id="workflow_block"
Start Program
   ↓
Authentication (Login / Signup)
   ↓
Role Detection (Admin / User)
   ↓
Load Book Data
   ↓
Show Role-Based Menu
   ↓
Perform Operations
   ↓
Save Data
   ↓
Exit
```

---

## 🔐 Role-Based Access Control

| Feature      | Admin | User |
| ------------ | ----- | ---- |
| Add Book     | ✅     | ❌    |
| View Books   | ✅     | ✅    |
| Search Books | ✅     | ✅    |
| Issue Book   | ❌     | ✅    |
| Return Book  | ❌     | ✅    |

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```bash id="clone_cmd"
git clone https://github.com/your-username/library-management-system.git
```

### 2️⃣ Navigate to project folder

```bash id="cd_cmd"
cd Library_management_system
```

### 3️⃣ Run the program

```bash id="run_cmd"
python main.py
```

---

## 📂 Initial Setup

### Create required files:

```text id="setup_files"
data.txt
users.txt
```

### Add default admin manually:

```text id="admin_setup"
admin,admin123,admin
```

---

## 💡 Key Concepts Implemented

* ✔ CRUD Operations
* ✔ Modular Programming
* ✔ Object-Oriented Programming (OOP)
* ✔ File Handling (Persistent Storage)
* ✔ Input Validation
* ✔ Exception Handling
* ✔ Role-Based Access Control (RBAC)

---

## 👨‍💻 Team Contribution

| Member   | Responsibility                     |
| -------- | ---------------------------------- |
| Member 1 | main.py (UI + Flow + Role Control) |
| Member 2 | model.py (OOP Design)              |
| Member 3 | service.py (CRUD Logic)            |
| Member 4 | file_handler.py & auth.py          |

---

## 🎯 Future Enhancements

* GUI using Tkinter
* Database integration (MySQL / MongoDB)
* Web version (React + Flask)
* Password encryption (hashing)
* Admin dashboard

---

## 🧠 Learning Outcomes

* Understanding modular project structure
* Implementing authentication & authorization
* Working with persistent storage
* Designing role-based systems
* Handling real-world edge cases

---

## 📌 Conclusion

This project demonstrates how core Python concepts can be combined to build a structured, scalable, and secure application.
With the addition of role-based access control, it closely simulates real-world system design.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
