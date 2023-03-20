from artist import Artist

class ArtistManager:
    '''Gestiona los objetos de la clase Artist en la base de datos'''

    def __init__(self,connection):
        self.__connection = connection
        self.__cursor = connection.cursor()

    def getByIds(self,*ids):
        '''Devuelve una colección de objetos tipo artist

            ids -> coleccion de ids correspondientes a artistas
            resultado -> devolvera una lista de tipo artist
        '''
        sql = 'SELECT id, nombre, nacionalidad, fecha_nacimiento '
        sql += 'FROM Artista '
        sql += 'WHERE id IN {}'.format(ids)
        self.__cursor.execute(sql)
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myArtist = Artist(self.__connection, row[0], row[1], row[2], row[3])
            result.add(myArtist)
        return result
    
    def getByName(self,name):
        '''Devuelve una colección de objetos tipo artist segun su nombre

            name -> contendrá parte del nombre de un artista(str)
            resultado -> devolvera una conjunto de objetos de tipo artist
        '''
        sql = 'SELECT id, nombre, nacionalidad, fecha_nacimiento '
        sql += 'FROM Artista '
        sql += 'WHERE lower(nombre) LIKE lower(?)'
        self.__cursor.execute(sql, ('%' +name+ '%',))
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myArtist = Artist(self.__connection, row[0], row[1], row[2], row[3])
            result.add(myArtist)
        return result
    
    def getByNacionality(self,nacionality):
        '''Devuelve una colección de objetos tipo artist segun su nacionalidad

            nacionality -> nacionalidad deseada(str)
            resultado -> devolvera una conjunto de objetos de tipo artist
        '''
        sql = 'SELECT id, nombre, nacionalidad, fecha_nacimiento '
        sql += 'FROM Artista '
        sql += 'WHERE lower(nacionalidad) LIKE lower(?)'
        self.__cursor.execute(sql, ('%' +nacionality+ '%',))
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myArtist = Artist(self.__connection, row[0], row[1], row[2], row[3])
            result.add(myArtist)
        return result
    
    def getBySongType(self,songType):
        '''Devuelve una colección de objetos tipo artist según de algunas de sus canciones

            songType -> Genero musica(str)
            resultado -> devolvera una conjunto de objetos de tipo artist
        '''
        sql = 'SELECT DISTINCT artista.id, nombre, nacionalidad, fecha_nacimiento '
        sql += 'FROM Artista '
        sql += 'JOIN Cancion On Artista.id = Cancion.id_artista WHERE lower(genero) LIKE lower(?)'
        self.__cursor.execute(sql, (f'%{songType}%',))
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myArtist = Artist(self.__connection, row[0], row[1], row[2], row[3])
            result.add(myArtist)
        return result