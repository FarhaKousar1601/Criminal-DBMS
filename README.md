# Criminal Database Management System

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=plastic)](https://www.python.org/downloads/)
[![SQLite Version](https://img.shields.io/badge/SQLite-3.35.5-green?style=plastic)](https://www.sqlite.org/download.html)
[![Tkinter Version](https://img.shields.io/badge/Tkinter-8.6-red?style=plastic)](https://docs.python.org/3/library/tkinter.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=plastic)](https://opensource.org/licenses/MIT)



The Criminal Database Management System is a Python application designed to manage criminal records efficiently. It provides functionalities to add, view, search, update, and delete criminal records stored in a SQLite database. The application utilizes the Tkinter library for the graphical user interface and SQLite3 for database management.

## Features

- **User Authentication:** The system provides a login interface to authenticate users before accessing the database functionalities.
- **CRUD Operations:** Users can perform CRUD (Create, Read, Update, Delete) operations on criminal records stored in the database.
- **Search Functionality:** Users can search for specific criminal records based on various criteria such as Criminal ID, Name, Gender, Nationality, Age, Height, Weight, and Crime Committed.
- **Graphical User Interface:** The application offers an intuitive GUI built using the Tkinter library, making it user-friendly and accessible.
- **Data Persistence:** Criminal records are stored persistently in a SQLite database, ensuring data integrity and availability across sessions.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/criminal-database.git
```

2. Navigate to the project directory:

```bash
cd criminal-database
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python main.py
```

## Usage

1. Launch the application by executing the `main.py` file.
2. Log in using valid credentials to access the database functionalities.
3. Use the navigation buttons to perform CRUD operations on criminal records.
4. Utilize the search functionality to find specific criminal records based on desired criteria.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
