from sport import Sport
from trainers import Trainers


class SportManager:
    ''''
    Gestiona los objetos de la clase Sport en la base de datos.
    NOTE: por ahora vacía porque no se si quieres incluir esta funcionalidad...
    '''
    
    def __init__(self, connection):
        self.__connection = connection
        self.__cursor = connection.cursor()

    def get_soprts_with_more_vacances(self):
        pass

    def get_all_saved_sports(self):
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
                Trainers(self.__connection, row[2], row[3], row[4])
            )
            result.add(sport)
            
        return result
