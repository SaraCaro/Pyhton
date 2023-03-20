from datetime import datetime
import sqlite3

class BookManager:
    def __init__(self, connection):
        self.__connection = connection
        self.__cursor = connection.cursor()

    def get_all_books_by_date_and_sport(self, date, sport):
        '''
        Obtener todas las reservas por fecha y deporte
        '''
        sql = 'SELECT * from book WHERE sport = ?'
        self.__cursor.execute(sql, (sport.getID(),))
        rows = self.__cursor.fetchall()
        rows_by_date = []
        for row in rows:
            if self.is_the_same_date(row[1], date):
                rows_by_date.append(row)

        return rows_by_date

    def is_the_same_date(self, date1, date2):
        splitted_date = date1.split(' ')
        date2_str = date2.strftime('%Y-%m-%d')
        return splitted_date[0] == date2_str
