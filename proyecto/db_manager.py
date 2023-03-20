import sqlite3

class DBManager:
    def __init__(self):
        self.__conn = sqlite3.connect('pabellon.db')

    def execute(self,query, data, is_write=False):
        '''
        Ejecutar una consulta contra la base de datos sqlite
        :param query: consulta sql
        :param data: tupla con la información
        :param is_write: para saber si es un insert, update o delete
        '''
        cursor = self.__conn.cursor()
        cursor.execute(query, data)
        if is_write: 
            self.__conn.commit()
        else: 
            rows = cursor.fetchall()
            return rows
        cursor.close()

    def __del__(self):
        print("Destructor called")
        self.__conn.close()
