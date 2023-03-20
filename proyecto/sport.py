from db_entity import DBEntity


class Sport:
    def __init__(self,conn, id=None, name=None, vacances=None):
        self.__conn = conn
        self.__id = id
        self.__name = name
        self.__vacances = vacances
    
    def __str__(self):
        result = f'El ID es: {self.__id} '
        if self.__name is not None:
            result += f' \nNombre: {self.__name}'
        if self.__vacances is not None:
            result += f' \nVacantes: {self.__vacances}\n'
        return result

    def getVacances(self):
        return self.__vacances
        
    def load(self):
        '''
        Carga los datos de la BD.
        '''
        sql = 'SELECT * FROM sports'
        return self._conn.execute(sql)
