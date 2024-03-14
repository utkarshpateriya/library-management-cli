# Library Management CLI Application

## Development Approach

### Code Structure

I began the project by implementing key functionalities outlined in `main.py`, focusing on components like `user_manager`, `book_manager`, and `checkout_manager`. To ensure clarity and maintainability, I carefully organized the code into distinct folders, facilitating a clear separation of concerns.

In response to the challenge of distinguishing between models and manager methods, I opted for a structured approach. This involved categorizing files into purposeful folders such as:
- `apps`
- `db`
- `logging`
- `models`
- `service`
- `utils`

# Library Management CLI Application Folder Structure

## `apps`

This folder houses the main executable files and serves as the entry point to the application. It encapsulates the core logic and orchestrates the interactions between different modules.

1. `library_app.py`-
   `user_menu(self)`: Displays and handles user-related menu options.
   `book_menu(self)`: Displays and handles book-related menu options.
   `run(self)`: Runs the main library management system loop, displaying and handling the main menu options.

## `db`

The `db` folder is designated for handling data storage and retrieval. It manages the persistence of application data, ensuring that user and book information is stored reliably and can be retrieved across application sessions.

1. `storage.py`-
   The `storage` class provides static methods for loading and saving data directly from/to the JSON file specified in the `Config` class.
   The `DataManager` class is designed to interact with the Storage class indirectly, allowing manipulation of data associated with a specific key.

## `logging`

In the `logging` folder, you'll find utilities for logging operations within the application. Logging is essential for tracking and recording various events, providing insights into the application's behavior and aiding in debugging.

## `models`

The `models` folder contains the data models representing key entities in the application, such as users and books. Each model defines the structure and behavior of its corresponding entity, facilitating a clear and organized representation of data.

## `service`

All the services provided by application i.e User Management, Book Management, Check in/out management have their logics in `service` folder. 

## `utils`

The `utils` folder houses utility functions and helper modules used across the application. These utilities provide reusable pieces of code that contribute to the efficiency and maintainability of the overall codebase.

## `cli.py` and `main.py`

These files, located in the root directory, serve as the entry points for the command-line interface (CommandLineInterFace) application. `command_line_interface.py` may contain functions related to user input and display, while `main.py` orchestrates the overall application flow.

This organizational strategy not only enhances code readability but also positions the project for scalable growth.

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/library-management-cli.git
   ```

2. **Navigate to the Project Directory:**
   
   ```bash
   cd library-management-cli
   ```
3. **Run the Application:**
   
   ```bash
   python main.py
   ```
There is a .env.example file that is an example of the .env file to be used. For initial run you can change the name from `.env.example` to `.env` to run.

# Usage

## Main Menu
**Upon running the application, you'll encounter the main menu with the following options:**

User Menu (`1`):

Create users, list existing users, search for users, and return to the main menu.
Book Menu (`2`):

Manage books, including adding books, listing books, searching for books, and performing check-in and check-out operations.
Exit (`0`):

Exit the Library Management System.

## User Menu
**When you choose option `1` from the main menu, you enter the User Menu. Here are the available options:**

Create User (`1`):

Add a new user by providing their name and user ID.
List Users (`2`):

Display a list of all existing users.
Search User (`3`):

Search for users by name or user ID.
Back to Main Menu (`0`):

Return to the main menu.


## Book Menu
**Selecting option `2` from the main menu takes you to the Book Menu. Here are the available options:**

Add Book (`1`):

Add a new book by providing the title, author, and ISBN.
List Books (`2`):

Display a list of all existing books.
Search Books (`3`):

Search for books by title, author, or ISBN.
Check Out Book (`4`):

Check out a book to a user by providing their user ID and the book's ISBN.
Check In Book (`5`):

Check in a book by providing the user ID and the book's ISBN.
Check Book Availability (`6`):

Check the availability of a book by providing its ISBN.
Back to Main Menu (`0`):

Return to the main menu.


**General CLI Usage**
Input:

Enter your choice by typing the corresponding number and pressing Enter.
Output:

Messages and information will be displayed on the command line.
Continue:

Some actions may prompt you to press Enter to continue.
Exiting the Application
Choose option `0` in the main menu to exit the Library Management System.