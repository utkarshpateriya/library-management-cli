"""
Contains all the models or entities used in our Library CLI Application.
"""

class Book:
    def __init__(self, title, author, isbn, availability=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability = availability


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id