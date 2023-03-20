from db_manager import DBManager

class DBEntity:
    '''
    Esta clase va a abstraer la operacion CRUD de la base de datos
    This class is going to abstact the database CRUD operation
    '''
    
    def __init__(self, conn, table_name):
        self._conn = conn 
        self._tablename = table_name

    def load(self):
        '''
        Carga los datos de la BD.
        '''
        
        sql = f'SELECT * FROM {self._tablename}'
        return self._conn.execute(sql, ())

    def insert(self, data):
        '''
        Carga los datos de un cliente en memoria.
        :param data: tupla de las columnas a insertar
        '''
        sql = f"INSERT INTO {self._tablename}('date', 'sport', 'trainer') VALUES (?, ?, ?)"
        return self._conn.execute(sql, data, is_write=True)
    
    def delete(self, data):
        '''
        Carga los datos de un cliente en memoria.
        :param data: tupla de las columnas a insertra
        '''
        sql = f"DELETE FROM {self._tablename} where id = ?"
        return self._conn.execute(sql, data, is_write=True)
