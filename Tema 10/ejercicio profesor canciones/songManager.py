import sqlite3

from artist import Artist
from disc import Disc
from song import Song

class SongManager:
    '''Gestiona los objetos de la clase Song en la base de datos'''

    def __init__(self,connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()

    def __getSong(self, row):
        '''
        Crea un objeto Song a partir de un registro de la base de datos
        row: registro de la base de datos (con informacion de canción, artista y disco)
        resultado: canción (Song)
        '''
        conn = self.__connection
        my_artist = None
        if row['id_artista'] is not None:
            my_artist = Artist(
                conn, 
                row['id_artista'], 
                row['nombre'], 
                row['nacionalidad'], 
                row['fecha_nacimiento']
            )
        my_disc = None
        if row['id_disco'] is not None:
             my_artist = Disc(
                conn, 
                row['id_disco'], 
                row['d_titulo'], 
                row['fecha'], 
                row['editor']                
            )

        my_song = Song(conn, 
            row['c_id'], 
            row['c_titulo'], 
            row['contenido'], 
            row['duracion'],
            row['genero'],
            my_artist,
            my_disc
        )
        return (my_song)
    
    def __getSongSet(self,rows):
        '''
        Crea una colección de canciones a partir de un registro de la base de datos
        row: lista de registro de la base de datos (con informacion de canción, artista y disco)
        resultado: canción (Song)
        '''
        result = set()
        if rows is None:
            return result
        for row in rows:
            my_song = self.__getSong(row)
            result.add(my_song)
        return result
    

    def getByIds(self,*ids):
        '''Obtiene las canciones correspondientes a los ids indicados

            ids -> coleccion de ids correspondientes a canciones en la base datos 
            resultado -> (set) objetos de la clase Song
        '''
        sql = 'SELECT Cancion.id AS c_id, Cancion.titulo AS c_titulo, duracion, genero, contenido, id_artista, id_disco, ' # cancion
        sql += 'nombre, nacionalidad, fecha_nacimiento, ' # artista
        sql += 'Disco.titulo AS d_titulo, fecha, editor ' # disco
        sql += 'FROM Cancion '
        sql += 'LEFT JOIN Artista ON Artista.id = Cancion.id_artista '
        sql += 'LEFT JOIN Disco ON Disco.id = Cancion.id_disco '
        if len(ids) > 1:
            sql += 'WHERE Cancion.id IN {} '.format(ids)
        elif len(ids) == 1:
            sql += f'WHERE Cancion.id = {ids[0]}'
        print(sql)
        self.__cursor.execute(sql)
        rows = self.__cursor.fetchall()
        return self.__getSongSet(rows)

    def getByTitle(self,title):
        '''Obtiene las canciones según el titulo indicado

            title -> titulo o parte de la canción (str)
            resultado -> colección de canciones (set)
        '''
        sql = 'SELECT Cancion.id AS c_id, Cancion.titulo AS c_titulo, duracion, genero, contenido, id_artista, id_disco, ' # cancion
        sql += 'nombre, nacionalidad, fecha_nacimiento, ' # artista
        sql += 'Disco.titulo AS d_titulo, fecha, editor ' # disco
        sql += 'FROM Cancion '
        sql += 'LEFT JOIN Artista ON Artista.id = Cancion.id_artista '
        sql += 'LEFT JOIN Disco ON Disco.id = Cancion.id_disco '
        sql += 'WHERE Cancion.titulo LIKE lower(?)'
        self.__cursor.execute(sql, (f'%{title}%',))
        rows = self.__cursor.fetchall()
        return self.__getSongSet(rows)
    
    def getByArtistIds(self,*artistIds):
        '''
        devuelve una colección de objetos tipo disc según su artista
        artistIds = contendrá el id de artistas de una canción(tuple)
        resultado = devolverá un conjunto de objetos tipo Canción 
        '''
        sql = 'SELECT Cancion.id AS c_id, Cancion.titulo AS c_titulo, duracion, genero, contenido, id_artista, id_disco, ' # cancion
        sql += 'nombre, nacionalidad, fecha_nacimiento, ' # artista
        sql += 'Disco.titulo AS d_titulo, fecha, editor ' # disco
        sql += 'FROM Cancion '
        sql += 'LEFT JOIN Artista ON Artista.id = Cancion.id_artista '
        sql += 'LEFT JOIN Disco ON Disco.id = Cancion.id_disco '
        if len(artistIds) > 1:
            sql += 'WHERE Cancion.id IN {}'.format(artistIds)
        elif len(artistIds) == 1:
            sql += 'WHERE Cancion.id = {}'.format(artistIds[0])

        self.__cursor.execute(sql, (f'%{artistIds}%',))
        rows = self.__cursor.fetchall()
        return self.__getSongSet(rows)
    
    def getBaseSQL(self):
        '''Contiene las consultas de songManager

            resultado -> devuelve el contenido de las consultas
        '''
        sql = 'SELECT Cancion.id AS c_id, Cancion.titulo AS c_titulo, duracion, genero, contenido, id_artista, id_disco, ' # cancion
        sql += 'nombre, nacionalidad, fecha_nacimiento, ' # artista
        sql += 'Disco.titulo AS d_titulo, fecha, editor ' # disco
        sql += 'FROM Cancion '
        sql += 'LEFT JOIN Artista ON Artista.id = Cancion.id_artista '
        sql += 'LEFT JOIN Disco ON Disco.id = Cancion.id_disco '