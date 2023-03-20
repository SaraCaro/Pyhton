# from Cancion import Cancion

class Artista:
    '''Representa a un Artista'''
    def __init__(self,connection,id=None,nombre=None,fecha_nac=None,nacionalidad=None):
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__id = id
        self.__nombre = nombre
        self.__fecha_nac = fecha_nac
        self.__nacionalidad = nacionalidad
    
    def __str__(self):
        return f'{self.__nombre} nació en {self.__fecha_nac} y es de nacionalidad {self.__nacionalidad}'
    
    def save(self):
        '''
        Añadir un nuevo Artista a la base de datos
        '''
        sql = 'INSERT INTO Artista (id, nombre, fecha_nac,nacionalidad) VALUES (?, ?, ?,?)'
        
        values = (
            self.__id,
            self.__nombre, 
            self.__fecha_nac,
            self.__nacionalidad
        )

        self.__cursor.execute(sql, values)
        self.__connection.commit()
    
    def delete(self):
        '''
        Borra un artitsa existente en la base de datos.
        '''
        sql = 'DELETE FROM Artista WHERE id = ?'

        self.__cursor.execute(sql, (self.__id,))
        self.__connection.commit()
    
    def update(self):
        '''
        Actualiza los datos de un artista existente en la base de datos.
        '''
        sql = 'UPDATE Artista SET nombre = ?, fecha_nac = ?, nacionalidad = ? WHERE id = ?'

        self.__cursor.execute(sql, (self.__nombre, self.__fecha_nac, self.__nacionalidad))
        self.__connection.commit()
    
    
    def load(self):
        '''
        Carga en memoria de la base de datos un artista
        '''
        sql = 'SELECT nombre, fecha_nac, nacionalidad FROM Artista WHERE id = ?'


        self.__cursor.execute(sql, (self.__id,))
        self.__cursor.execute(sql,(self.__id,))
        row = self.__cursor.fetchone()
        self.__nombre = row[0]
        self.__fecha_nac = row[1]
        self.__nacionalidad = row[2]

    def getId(self):
        return self.__id
    
    def getnombre(self):
        return self.__nombre
    
    def getfecha_nac(self):
        return self.__fecha_nac

    def getnacionalidad(self):
        return self.__nacionalidad

