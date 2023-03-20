import sqlite3

from disc import Disc

class DiscManager:
    '''Gestiona los objetos de la clase Disco en la base de datos'''

    def __init__(self,connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()

    def getByIds(self,*ids):
        '''Devuelve una colección de objetos tipo disc

            ids -> coleccion de ids correspondientes a discos
            resultado -> devolvera una lista de tipo disc
        '''
        sql = 'SELECT id, titulo, fecha, editor '
        sql += 'FROM Disco '
        sql += 'WHERE id IN {}'.format(ids)
        self.__cursor.execute(sql)
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myDisc = Disc(self.__connection, row[0], row[1], row[2], row[3])
            result.add(myDisc)
        return result
    
    def getByTitle(self,title):
        '''Devuelve una colección de objetos tipo disc

            title -> coleccion de titulos correspondientes a discos
            resultado -> devolvera una lista de tipo disc
        '''
        sql = 'SELECT id, titulo, fecha, editor '
        sql += 'FROM Disco '
        sql += 'WHERE lower(titulo) LIKE lower(?)'
        self.__cursor.execute(sql, (f'%{title}%',))
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myDisc = Disc(self.__connection, row[0], row[1], row[2], row[3])
            result.add(myDisc)
        return result
    
    def getByYear(self,year):
        '''Devuelve una colección de objetos tipo disc

            year -> año de publicación del disco(int)
            resultado -> devolvera una lista de tipo disc
        '''
        sql = 'SELECT id, titulo, fecha, editor '
        sql += 'FROM Disco '
        sql += 'WHERE fecha like ?'
        self.__cursor.execute(sql, (f'{year}-%',))
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myDisc = Disc(self.__connection, row[0], row[1], row[2], row[3])
            result.add(myDisc)
        return result
    
    def getAfter(self,year):
        '''Devuelve una colección de objetos tipo disc a partir de ese año

            year -> año apartir del cual se ha publicado el disco(str)
            resultado -> devolvera una lista de tipo disc
        '''
        sql = 'SELECT id, titulo, fecha, editor '
        sql += 'FROM Disco '
        sql += 'WHERE fecha >= ?'
        self.__cursor.execute(sql, (f'{year}-%',))
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myDisc = Disc(self.__connection, row[0], row[1], row[2], row[3])
            result.add(myDisc)
        return result
    
    def getByPublisher(self,publisher):
        '''
        devuelve una coleccion de objetos tipo disc segun su editor
        publisher = contendrá parte del nombre del editor de un disco(str)
        resultado = devolverá un conjunto de objetos
        '''
        sql = 'SELECT id, titulo, fecha, editor '
        sql += 'FROM Disco '
        sql += 'WHERE lower(editor) LIKE lower(?)'
        self.__cursor.execute(sql, (f'%{publisher}%',))
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myDisc = Disc(self.__connection, row['id'], row['titulo'], row['fecha'], row['editor'])
            result.add(myDisc)
        return result
    
    def getByArtistIds(self,*artistIds):
        '''
        devuelve una colección de objetos tipo disc según su artista
        artistIds = contendrá el id de artistas de un disco(tuple)
        resultado = devolverá un conjunto de objetos tipo Disc 
        '''
        sql = 'SELECT Disco.id as disco_id, Disco.titulo, fecha, editor '
        sql += 'FROM Disco,Artista '
        sql += 'JOIN Cancion on Cancion.id_disco = disco.id '
        sql += 'JOIN Artista on Artista.id = Cancion.id_artista '
        if len(artistIds) > 1:
            sql += 'WHERE Artista.id IN {}'.format(artistIds)
        elif len(artistIds) == 1:
            sql += 'WHERE Artista.id = {}'.format(artistIds[0])
        self.__cursor.execute(sql, (f'%{artistIds}%',))
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myDisc = Disc(self.__connection, row['disco_id'], row['titulo'], row['fecha'], row['editor'])
            result.add(myDisc)
        return result
    
    def getByTypes(self,*types):
        '''
        devuelve una colección de objetos tipo disc según su genero
        types = contendrá el genero/s de una cancion de un disco(tuple)
        resultado = devolverá un conjunto de objetos tipo Disc 
        '''
        sql = 'SELECT Disco.id as disco_id, Disco.titulo as disco_titulo, fecha, editor '
        sql += 'FROM Disco,Artista '
        sql += 'JOIN Cancion on Cancion.id_disco = disco.id '
        data = ()
        if len(types) > 1:
            my_types = self.lowerTuple(types)
            sql += 'WHERE lower(Cancion.genero) in {} '.format(my_types)
        elif len(types) == 1:
            data = (types[0],)
            sql += 'WHERE lower(Cancion.genero) = lower(?)'
        self.__cursor.execute(sql, data)
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myDisc = Disc(self.__connection, row['disco_id'], row['titulo'], row['fecha'], row['editor'])
            result.add(myDisc)
        return result
    
    def lowerTuple(self,types):
        '''
        devuelve la tupla que se le pasa por parámetro con sus valores en minúsculas
        '''

        types_lower = []
        for my_type in types:
            types_lower.append(my_type.lower())
        return tuple(types_lower)