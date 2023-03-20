
from trainers import Trainers


class Sport:
    def __init__(self,conn, id=None, name=None, vacances=None, trainer=None):
        self.__conn = conn
        self.__cursor = conn.cursor()
        self.__id = id
        self.__name = name
        self.__vacances = vacances
        self.__trainer = trainer
    
    def __str__(self):
        result = f'El ID es: {self.__id} '
        if self.__name is not None:
            result += f' \nNombre: {self.__name}'
        if self.__vacances is not None:
            result += f' \nVacantes: {self.__vacances}'
        if self.__trainer is not None:
            result += f' \nEntrenador es: {self.__trainer.getID()}\n'
        return result

    def getVacances(self):
        return self.__vacances
    
    def getID(self):
        return self.__id
    
    def load(self):
        '''
        Carga en memoria un deporte de la base de datos.
        '''
        if self.__id is None:
            raise TypeError('El atributo id debe tener valor')

        sql = 'SELECT name, vacances, trainer, Trainers.nombre, Trainers.phone '
        sql += 'FROM Sports INNER JOIN Trainers ON Sports.trainer = Trainers.id '
        sql += 'WHERE Sports.id = ?'
        self.__cursor.execute(sql, (self.__id,))
        row = self.__cursor.fetchone()
        self.__name = row[0]
        self.__vacances = row[1]
        self.__trainer = Trainers(self.__conn, row[2], row[3], row[4])
