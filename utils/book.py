from db.storage import DataManager
from models.library_models import Book
from cli import CLI

class BookManager(DataManager):
    """
    Contains all the methods required to CRUD Books in Library CLI Application
    """
    def __init__(self):
        super().__init__("books")

    def add_book(self, title, author, isbn):
        data = self.get_data()
        if self.isbn_is_unique(isbn):
            new_book = Book(title, author, isbn)
            data.append(vars(new_book))
            self.save_data(data)
            CLI.display_message("Book entry created!")
            # Log the book addition operation
            self.logger.log_book_added(self, title, author, new_book.isbn)
        else:
            CLI.display_message("Invalid isbn. Already assigned to other book")

    def list_books(self):
        data = self.get_data()
        for book_data in data:
            book = Book(**book_data)
            CLI.display_message(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Available: {book.availability}")

    def search_books(self, keyword):
        data = self.get_data()
        results = [Book(**book_data) for book_data in data if
                   keyword.lower() in book_data["title"].lower() or
                   keyword.lower() in book_data["author"].lower() or
                   keyword.lower() in book_data["isbn"].lower()]
        for result in results:
            CLI.display_message(f"Title: {result.title}, Author: {result.author}, ISBN: {result.isbn}, Available: {result.availability}")

    def is_available(self, isbn):
        data = self.get_data()
        book = [Book(**book_data) for book_data in data if                   
                   isbn.lower() in book_data["isbn"].lower()]
        if book:
            book = book[0]
            if book.availability:
                CLI.display_message(f"Book with Title: {book.title}, Author: {book.author} is available")
            else:
                CLI.display_message(f"Book with Title: {book.title}, Author: {book.author} is not available")
        else:
            CLI.display_message(f"Book with isbn: {isbn} does not exist")

    def isbn_is_unique(self, isbn):
        """
        Checks if isbn provided is already in db or not.
        """
        data = self.get_data()
        book = [Book(**book_data) for book_data in data if                   
                   isbn.lower() in book_data["isbn"].lower()]       
        if len(book) > 0:
            return False
        else:
            return True