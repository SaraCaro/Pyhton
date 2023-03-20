from book_manager import BookManager
from sport import Sport
from trainers import Trainers
import datetime

class Book:
    def __init__(self,conn, id=None,date=None, sport=None, trainer=None):
        super().__init__(conn, 'book')
        self.__conn = conn
        self.__id = id
        self.__date = date
        self.__sport = sport
        self.__trainer = trainer

    def getSport(self):
        return self.__sport
    
    def getDate(self):
        return self.__date

    def load(self):
        '''
        Carga la reserva con el self.__id guardado.
        ''' 
        sql = 'SELECT * FROM book inner join sports on sports.id = book.sport inner join trainers on book.trainer = trainers.id WHERE sport.id = ?'
        row = self._conn.execute(sql, (self.__id,))[0]
        self.__id = row[0]
        self.__date = row[1]
        self.__sport = Sport(self.__connection, row[2], row[3], row[4])
        self.__trainer = Trainers(self.__connection, row[5], row[6], row[7], row[8])

    def _available_time(self, date, sport, trainer):
        """
        Hay un entrenador por cada deporte
        Para saber si hay suficientes salas solo tenemos
        que mirar si hay reservas en ese dia.
        :return: un mensaje del tipo `error_handler`
        """
        manager = BookManager(self.__conn)
        books = manager.get_all()
        print(books)
        book_filtered_sport = []
        for b in books:
            if b.getSport() == sport:
                book_filtered_sport.append(b)

        if len(book_filtered_sport) > 1:
            for b in book_filtered_sport:
                print(f"{date} , {b.getDate()}")
                if date == b.getDate():
                    return 1

        # Comprobar si hay plazas vacantes
        books_filteres_date = []
        for book in books:
            if book.getDate() == date:
                books_filteres_date.append(book)

        if len(books_filteres_date) > sport.getVacances():
            return 2

        return 0

    def insert(self, date, sport, trainer):
        if self._available_time(date, sport, trainer) == 0:
            print('guardado en la db')
            return super().insert((date, sport, trainer,))
        else:
            print('horario ya reservado')

    def remove(self, id_book):
        super().delete((id_book,))

def error_handler(error_id):
    return {
        0: 'Reserva correcta',
        1: 'Horario ya reservado',
        2: 'Sala llena'
    }

    