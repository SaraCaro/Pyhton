import imp
from sport import Sport
from datetime import datetime
from exceptions import OldDateException
from exceptions import FullClassInThisSport
from bookManager import BookManager

class Book:
    def __init__(self,conn, id=None,date=None, sport=None):
        self.__conn = conn
        self.__cursor = conn.cursor()
        self.__id = id
        self.__date = date
        self.__sport = sport

    def getSport(self):
        return self.__sport
    
    def getDate(self):
        return self.__date

    @classmethod
    def check_hours_format(cls, time):
        t = time.split(' ') # [12/12/2012, 10:45]
        return t[1] in ['16:00', '17:00', '18:00', '19:00', '20:00']

    def load(self):
        '''
        Carga en memoria una reserva de la base de datos.
        '''
        if self.__id is None:
            raise TypeError('El atributo id debe tener valor')
        
        sql = 'SELECT date, sport FROM book '
        sql += 'WHERE id = ?'
        self.__cursor.execute(sql, (self.__id,))
        row = self.__cursor.fetchone()
        self.__date = datetime.strptime(row[0], '%d/%m/%Y %H:%M:%S')
        self.__sport = Sport(self.__conn, row[1]).load()

    def __str__(self):
        result = f'El ID es: {self.__id} '
        if self.__date is not None:
            result += f' \nFecha: {self.__date}'
        if self.__sport is not None:
            result += f' \nDeporte: {self.__sport}\n'
        return result

    def save(self):
        """
        Comprueba que se puede guardar el objeto Book:
        1. Que la fecha es posterior a la actual
        2. Que no hay ya reservar en esa fecha:
            2.1. Que coincide el deporte
            2.2. Que coincide la fecha
            2.3. Que hay vacantes disponibles
        """
        if self.__date < datetime.now():
            raise OldDateException()

        manager = BookManager(self.__conn)
        books_by_date_sport = manager.get_all_books_by_date_and_sport(self.__date, self.__sport)
        
        if self.__sport.getVacances() < len(books_by_date_sport):
            raise FullClassInThisSport()

        self.__save()


    def __save(self):
        '''
        Guarda una reserva en la base de datos
        '''
        sql = 'INSERT INTO book(date, sport) VALUES (?,?)'
        sport = self.__sport.getID() if self.__sport.getID() is not None else None
        values = (self.__date, sport)
        self.__cursor.execute(sql, values)
        self.__conn.commit()


def error_handler(error_id):
    return {
        0: 'Reserva correcta',
        1: 'Horario ya reservado',
        2: 'Sala llena'
    }

    