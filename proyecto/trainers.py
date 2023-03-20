from db_entity import DBEntity

class Trainers(DBEntity):
    def __init__(self,conn,id=None,name=None,phone=None,sport=None):
        super().__init__(conn, 'trainers')
        self.__conn = conn
        self.__id = id
        self.__name = name
        self.__phone = phone
        self.__sport = sport
    
    def __str__(self):
        result = f'El ID es: {self.__id} '
        if self.__name is not None:
            result += f' \nNombre: {self.__name}'
        if self.__phone is not None:
            result += f' \nTeléfono: {self.__phone}'
        if self.__sport is not None:
            result += f' \nVacantes: {self.__sport}\n'
        return result
    
    def load(self):
        '''
        Carga los datos de la BD.
        '''
        
        sql = f'SELECT * FROM {self._tablename}'
        return self._conn.execute(sql, ())
        