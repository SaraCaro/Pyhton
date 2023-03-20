from sport import Sport
from trainers import Trainers
import sqlite3

class SportManager:
    ''''
    Gestiona los objetos de la clase Sport en la base de datos.
    '''
    
    def __init__(self, connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()


    def get_all_saved_sports(self):
        '''
        Obtener todos los deportes
        '''
        sql = 'SELECT sports.id,name, vacances, trainer, trainers.nombre, trainers.phone FROM Sports '
        sql += 'INNER JOIN trainers ON sports.trainer = trainers.id'
        self.__cursor.execute(sql)
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            sport = Sport(
                self.__connection, 
                row[0], 
                row[1], 
                row[2],
                Trainers(self.__connection, row[3], row[4], row[5])
            )
            result.add(sport)
            
        return result
    
    def get_max_vacances(self):
        '''
        Obtener el deporte con el mayor numero de vacantes
        '''
        sql = 'SELECT id, name, vacances FROM Sports '
        sql += 'WHERE vacances = (SELECT MAX(vacances) FROM sports)'
        self.__cursor.execute(sql)
        row = self.__cursor.fetchone()
        result = set()
        sport = Sport(
            self.__connection, 
            row[0], 
            row[1], 
            row[2]
        )
        result.add(sport)
            
        return result

