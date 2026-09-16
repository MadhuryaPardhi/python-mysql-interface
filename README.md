# Python MySQL Database Manager

A command-line Python application developed as a Class XII Computer Science project to provide a simple interface for managing MySQL databases without requiring users to manually write SQL queries.

> **Project:** Python-MySQL Interface
> **Academic Year:** 2024–25
> **Language:** Python
> **Database:** MySQL

## 📌 About the Project

Working directly with MySQL usually requires knowledge of SQL commands. This project was created to simplify basic database management by providing a **menu-driven command-line interface (CLI)**.

The application accepts simple user inputs and performs the corresponding MySQL operations in the background.

The project focuses on basic database and table management, including **CRUD operations**, database creation/deletion, database switching, and basic password protection.

## ✨ Features

### Database Management

* Create a new database
* Switch between available databases
* Password-protect databases
* Drop/delete databases after password verification
* Maintain a list of available databases
* Store database/password information using a binary file

### Table Management

* Create tables
* View table data
* Insert records
* Update records
* Delete records
* Drop tables
* Automatically retrieve table column names

### User Interface

* Menu-driven command-line interface
* Simple numeric commands for operations
* Formatted database output using PrettyTable
* Basic input validation and error handling

## 🛠️ Technology Stack

| Technology                 | Purpose                                           |
| -------------------------- | ------------------------------------------------- |
| **Python**                 | Application logic and CLI                         |
| **MySQL**                  | Relational database                               |
| **mysql-connector-python** | Python–MySQL connection                           |
| **Pickle**                 | Storing/loading database records in binary format |
| **PrettyTable**            | Formatting query results                          |

## 🔄 How It Works

The basic application flow is:

```text
                    Start
                      │
                      ▼
             Load Database Records
                  from dbs.bin
                      │
                      ▼
                Choose Database
                      │
             ┌────────┴────────┐
             │                 │
          GUEST            Protected DB
             │                 │
             │          Check Password
             │                 │
             └────────┬────────┘
                      ▼
                MySQL Database
                      │
                      ▼
              Select an Operation
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
   Table Ops      Database Ops      Exit
```

## 🔐 Database Password System

The application maintains database names and their associated passwords in a Python dictionary called `AVAL_DB`.

When a database is created, its password is added to this dictionary and the dictionary is saved to a binary file named **`dbs.bin`** using Python's `pickle` module.

Conceptually, the stored data could look like:

```python
{
    "GUEST": "",
    "Stationery": "pen@copy"
}
```

The project uses:

```python
pickle.dump(AVAL_DB, F)
```

to save the information and:

```python
pickle.load(F)
```

to load it when the program starts.

### `CheckPassword()`

The original project source is incomplete and the implementation of `CheckPassword()` is missing.

However, its purpose can be determined from the remaining code.

The function is called when:

1. A user attempts to access a password-protected database.
2. A user attempts to delete/drop a protected database.

Its intended logic was approximately:

```text
Database name + Entered password
             │
             ▼
     Look up stored password
          in AVAL_DB
             │
             ▼
        Compare passwords
             │
       ┌─────┴─────┐
       │           │
     Match      No Match
       │           │
     True        False
       │           │
    Allow       Deny
```

The exact original implementation cannot be confirmed because that function is missing from the available source.

## 📋 Available Operations

The main menu provides the following options:

```text
1. TO CREATE A NEW TABLE
2. TO SELECT DATA FROM TABLE
3. TO INSERT DATA INTO TABLE
4. TO UPDATE DATA IN TABLE
5. TO DELETE DATA FROM TABLE
6. TO DROP A TABLE
7. TO CREATE A DATABASE
8. TO CHANGE THE DATABASE
9. TO DROP A DATABASE
0. Exit
```

## 💻 Example

The project demonstrates creating a database called `Stationery` with a password, creating an `Items` table, inserting records, viewing the records, updating data, deleting records, and eventually deleting the database.

Example table structure:

```text
Items
--------------------------------
Sno | Name          | Quantity | Price
--------------------------------
1   | Pentonic Pen  | 10       | 100
2   | Fountain Pen  | 5        | 250
3   | CardBoard     | 10       | 300
4   | Notebook      | 20       | 500
```

## 📂 Suggested Project Structure

```text
python-mysql-database-manager/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
└── dbs.bin
```

> **Note:** `dbs.bin` should generally not be committed to a public repository if it contains actual passwords.

## ⚙️ Requirements

* Python 3.11+
* MySQL 5.x or compatible MySQL installation
* `mysql-connector-python`
* `prettytable`

Install the Python dependencies with:

```bash
pip install mysql-connector-python prettytable
```

## 🚀 Running the Project

1. Install Python and MySQL.
2. Install the required Python packages.
3. Configure the MySQL connection in the Python program.
4. Run the application:

```bash
python main.py
```

5. Use the command-line menu to manage databases and tables.

## ⚠️ Project Status

**Archived / Educational Project**

This repository contains an old Class XII Computer Science project. The available source code is incomplete and may require restoration or modification before it can run correctly.

In particular:

* The original `CheckPassword()` implementation is missing.
* The project was designed for local MySQL usage.
* The original code contains hard-coded database connection credentials that should **not** be reused in a real application.
* Passwords were stored using `pickle`, which was suitable for demonstrating file handling in the school project but is **not a recommended approach for securely storing passwords in modern applications**.
* The project was designed for basic database operations rather than production use.

## 📚 Project Objectives

The original project aimed to:

* Provide basic CRUD operations.
* Abstract SQL complexity from the user.
* Provide a simple command-line interface.
* Implement basic error handling and data validation.
* Create a structure that could potentially be extended with more advanced features.

## 🎓 Project Background

This project was originally developed as a **Class XII Computer Science project** for the academic year **2024–25**.

It was submitted as a **Python-MySQL Interface** project and focused on demonstrating Python's ability to interact with a relational database through `mysql.connector`.

## 📖 References

* Python — https://www.python.org/
* MySQL — https://www.mysql.com/
* PrettyTable — https://pypi.org/project/prettytable/
* MySQL Connector/Python — https://pypi.org/project/mysql-connector-python/

---

**Built as a school Computer Science project • 2024–25**
