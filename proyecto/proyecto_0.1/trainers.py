
class Trainers:
    def __init__(self,conn,id=None,name=None,phone=None,sport=None):
        self.__conn = conn
        self.__cursor = conn.cursor()
        self.__id = id
        self.__name = name
        self.__phone = phone

    def __str__(self):
        result = f'El ID es: {self.__id} '
        if self.__name is not None:
            result += f' \nNombre: {self.__name}'
        if self.__phone is not None:
            result += f' \nTeléfono: {self.__phone}\n'
        return result
    
    def getID(self):
        return self.__id
    
    def load(self):
        '''
        Carga en memoria un Trainers de la base de datos.
        '''
        if self.__id is None:
            raise TypeError('El atributo id debe tener valor')

        sql = 'SELECT nombre, phone '
        sql += 'FROM Trainers '
        sql += 'WHERE Trainers.id = ?'
        self.__cursor.execute(sql, (self.__id,))
        row = self.__cursor.fetchone()
        self.__name = row[0]
        self.__phone = row[1]
