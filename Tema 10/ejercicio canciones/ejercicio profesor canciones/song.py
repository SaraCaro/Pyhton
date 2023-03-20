from artist import Artist
from disc import Disc

class Song:
    '''
    Representa a un disco perteneciente a un artista musical.
    '''

    def __init__(self, connection, song_id=None, title=None, content=None, duration=None, gender=None, artist_id=None,disk_id=None):
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__id = song_id
        self.__title = title
        self.__content = content
        self.__duration = duration
        self.__gender = gender
        self.__artist_id = artist_id
        self.__disk_id = disk_id


    def save(self):
        '''
        Añade un nueva canción  a la base de datos.
        '''
        sql = 'INSERT INTO Cancion (id, titulo, duracion, genero, contenido, id_artista, id_disco) '
        sql += 'VALUES (?, ?, ?, ?, ?, ?, ?)'
        values = (
            self.__id,
            self.__title,
            self.__content,
            self.__duration,
            self.__gender,
            self.__artist_id.getId(),
            self.__disk_id.getId(),
        )
        self.__cursor.execute(sql, values)
        self.__connection.commit()


    def delete(self):
        '''
        Borra una cancion existente en la base de datos.
        '''
        sql = 'DELETE FROM Cancion WHERE id = ?'
        self.__cursor.execute(sql, (self.__id,))
        self.__connection.commit()
    

    def update(self):
        '''
        Actualiza los datos de una canción existente en la base de datos.
        '''
        sql = 'UPDATE Cancion SET titulo = ?, contenido = ?, duracion = ?, genero = ?, id_artista = ?, id_disco = ? '
        sql += 'WHERE id = ?'
        values = (
            self.__title,
            self.__content,
            self.__duration,
            self.__gender,
            self.__artist_id.getId(),
            self.__disk_id.getId(),
            self.__id,
        )
        self.__cursor.execute(sql, values)
        self.__connection.commit()
    

    def load(self):
        '''
        Carga en memoria una canción de la base de datos.
        '''
        if self.__id is None:
            raise TypeError('El atributo id debe tener valor')
        sql = 'SELECT titulo, duracion, genero, contenido, id_artista, id_disco, '
        sql += 'nombre, nacionalidad, fecha_nacimiento, '
        sql += 'titulo, fecha, editor '
        sql += 'FROM Cancion'
        sql += 'JOIN Artista Artista.id = Cancion.id_artista '
        sql += 'JOIN Artista Disco.id = Cancion.id_disco '
        sql += 'WHERE id = ?'
        self.__cursor.execute(sql, (self.__id,))
        row = self.__cursor.fetchone()
        self.__title = row[0] # Investigar cómo utilizar claves textuales
        self.__content = row[1] 
        self.__duration = row[2] 
        self.__gender = row[3] 
        self.__artist_id = Artist(self.__connection, row[4], row[6], row[7], row[8])
        self.__disk_id = Disc(self.__connection, row[5], row[9], row[10], row[11]) 