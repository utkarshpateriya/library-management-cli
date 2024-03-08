import logging
from apps.library_app import LibraryApp

logging.basicConfig(filename='library.log', level=logging.INFO, format='%(asctime)s - %(message)s')

if __name__ == "__main__":
    app = LibraryApp()
    app.run()