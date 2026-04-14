# 📚 Library Management System (Console-Based Python Project)

## 📌 Project Overview

The **Library Management System** is a menu-driven console application developed using Python.
It allows users to manage books efficiently by performing operations like adding, viewing, searching, issuing, and returning books.

The system also includes:

* 🔐 User Authentication (Login & Signup)
* 💾 File Handling for data persistence
* 🧠 Object-Oriented Programming (OOP)
* ⚠️ Exception Handling and Input Validation

---

## 🚀 Features

### 📖 Book Management

* Add new books
* View all books
* Search books by title
* Issue books
* Return books

### 🔐 Authentication System

* User Signup (stored in `users.txt`)
* User Login validation

### 💾 File Handling

* Data stored in `data.txt`
* Persistent storage across program runs

### ⚙️ Error Handling

* Handles invalid inputs
* Prevents duplicate entries
* Skips corrupted/empty file data

---

## 🧱 Project Structure

```
Library_management_system/
│
├── main.py            # Main program (menu + flow control)
├── model.py           # Classes (Book, Library)
├── service.py         # Business logic (CRUD operations)
├── file_handler.py    # File handling (load/save data)
├── auth.py            # Login & Signup system
├── data.txt           # Book storage
├── users.txt          # User credentials
```

---

## 🧠 Technologies Used

* Python (Core Python)
* File Handling (`.txt`)
* Object-Oriented Programming (OOP)
* Exception Handling

---

## 🔄 Workflow

1. Start program
2. Login or Signup
3. Load book data from file
4. Perform operations (CRUD)
5. Save data automatically
6. Exit

---

## ▶️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/library-management-system.git
```

2. Navigate to project folder:

```bash
cd Library_management_system
```

3. Run the program:

```bash
python main.py
```

---

## 📂 Initial Setup

* Create empty files:

```
data.txt
users.txt
```

---

## 💡 Key Concepts Implemented

* ✔ CRUD Operations
* ✔ Modular Programming
* ✔ OOP (Classes & Objects)
* ✔ File Handling
* ✔ Input Validation
* ✔ Exception Handling

---

## 👨‍💻 Team Contribution

| Member   | Responsibility            |
| -------- | ------------------------- |
| Member 1 | main.py (UI & Flow)       |
| Member 2 | model.py (OOP Design)     |
| Member 3 | service.py (CRUD Logic)   |
| Member 4 | file_handler.py & auth.py |

---

## 🎯 Future Enhancements

* GUI using Tkinter
* Database integration (MySQL / MongoDB)
* Web version (React + Flask)
* Password encryption

---

## 🧠 Learning Outcomes

* Understanding real-world project structure
* Working with modular Python applications
* Implementing authentication systems
* Handling persistent data storage

---

## 📌 Conclusion

This project demonstrates how core Python concepts can be combined to build a structured and scalable application.
It is a beginner-to-intermediate level project that simulates real-world system design.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
