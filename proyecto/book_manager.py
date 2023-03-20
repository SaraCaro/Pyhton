from sport import Sport
from trainers import Trainers
from book import Book


class BookManager:
    def __init__(self, connection):
        self.__connection = connection


    def get_all_books(self):
        sql = 'SELECT * FROM book inner join sports on sports.id = book.sport inner join trainers on book.trainer = trainers.id'
        out = self._conn.execute(sql)
        result = set()
        for row in out:
            _id = row[0]
            _date = row[1]
            _sport = Sport(self.__connection, row[2], row[3], row[4])
            _trainer = Trainers(self.__connection, row[5], row[6], row[7], row[8])
            result.append(Book(self.__connection, _id, _date, _sport, _trainer))
        return result


