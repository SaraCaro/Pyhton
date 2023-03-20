from sport import Sport
from book import Book


class BookManager:
    def __init__(self, connection):
        self.__connection = connection
        self.__cursor = connection.cursor()


    def get_all_books(self):
        pass

