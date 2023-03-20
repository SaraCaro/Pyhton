class Disc:
    '''
    Representa a un disco perteneciente a un artista musical.
    '''
    
    def __init__(self, connection, disc_id=None, title=None, pubdate=None, publisher=None):
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__id = disc_id
        self.__title = title
        self.__pubdate = pubdate
        self.__publisher = publisher


    def save(self):
        '''
        Añade un nuevo disco a la base de datos.
        '''
        sql = 'INSERT INTO Disco (id, titulo, fecha, editor) '
        sql += 'VALUES (?, ?, ?, ?)'
        values = (
            self.__id,
            self.__title,
            self.__pubdate,
            self.__publisher,
        )
        self.__cursor.execute(sql, values)
        self.__connection.commit()


    def delete(self):
        '''
        Borra un disco existente en la base de datos.
        '''
        sql = 'DELETE FROM Disco WHERE id = ?'
        self.__cursor.execute(sql, (self.__id,))
        self.__connection.commit()
    

    def update(self):
        '''
        Actualiza los datos de un disco existente en la base de datos.
        '''
        sql = 'UPDATE Disco SET titulo = ?, fecha = ?, editor = ? '
        sql += 'WHERE id = ?'
        values = (
            self.__title,
            self.__pubdate,
            self.__publisher,
            self.__id,
        )
        self.__cursor.execute(sql, values)
        self.__connection.commit()
    

    def load(self):
        '''
        Carga en memoria un disco de la base de datos.
        '''
        if self.__id is None:
            raise TypeError('El atributo id debe tener valor')
        sql = 'SELECT titulo,fecha,editor '
        sql += 'FROM Disco '
        sql += 'WHERE id = ?'
        self.__cursor.execute(sql, (self.__id,))
        row = self.__cursor.fetchone()
        self.__title = row[0] # Investigar cómo utilizar claves textuales
        self.__pubdate = row[1] 
        self.__publisher = row[2]
    
    def getId(self):
        return self.__id
