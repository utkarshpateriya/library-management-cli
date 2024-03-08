import logging

class LibraryLogger:
    def __init__(self):
        logging.basicConfig(filename='library.log', level=logging.INFO, format='%(asctime)s - %(message)s')

    def log_book_added(self, title, author, isbn):
        logging.info(f"Book added: Title: {title}, Author: {author}, ISBN: {isbn}")

    def log_user_added(self, name, user_id):
        logging.info(f"User added: Name: {name}, User ID: {user_id}")

    def log_book_checked_out(self, title, user_id):
        logging.info(f"Book checked out: Title: {title}, User ID: {user_id}")

    def log_book_checked_in(self, title, user_id):
        logging.info(f"Book checked in: Title: {title}, User ID: {user_id}")