class Artist:
    '''
    Representa a un artista musical, individual o grupo.
    '''

    def __init__(self, connection, artist_id=None, name=None, country=None, birthdate=None):
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__id = artist_id
        self.__name = name
        self.__country = country
        self.__birthdate = birthdate

    def __str__(self):
        return f'\nEl artista con id {self.__id} y nombre = {self.__name}'

    def save(self):
        '''
        Añade un nuevo artista a la base de datos.
        '''
        sql = 'INSERT INTO Artista (id, nombre, nacionalidad, fecha_nacimiento) '
        sql += 'VALUES (?, ?, ?, ?)'
        values = (
            self.__id,
            self.__name,
            self.__country,
            self.__birthdate,
        )
        self.__cursor.execute(sql, values)
        self.__connection.commit()


    def delete(self):
        '''
        Borra un artista existente en la base de datos.
        '''
        sql = 'DELETE FROM Artista WHERE id = ?'
        self.__cursor.execute(sql, (self.__id,))
        self.__connection.commit()
    

    def update(self):
        '''
        Actualiza los datos de un artista existente en la base de datos.
        '''
        sql = 'UPDATE Artista SET nombre = ?, nacionalidad = ?, fecha_nacimiento = ? '
        sql += 'WHERE id = ?'
        values = (
            self.__name,
            self.__country,
            self.__birthdate,
            self.__id,
        )
        self.__cursor.execute(sql, values)
        self.__connection.commit()
    

    def load(self):
        '''
        Carga en memoria un artista de la base de datos.
        '''
        if self.__id is None:
            raise TypeError('El atributo id debe tener valor')
        sql = 'SELECT nombre, nacionalidad, fecha_nacimiento '
        sql = 'SELECT nombre, nacionalidad, fecha_nacimiento '
        sql += 'FROM Artista '
        sql += 'WHERE id = ?'
        self.__cursor.execute(sql, (self.__id,))
        row = self.__cursor.fetchone()
        self.__name = row[0]    # Investigar cómo utilizar claves textuales
        self.__country = row[1]
        self.__birthdate = row[2]

    def reload(self):
        '''
        Carga en memoria un artista de la base de datos.
        '''
        if self.__id is None:
            raise TypeError('El atributo id debe tener valor')
        sql = 'SELECT nombre, nacionalidad, fecha_nacimiento '
        sql = 'SELECT nombre, nacionalidad, fecha_nacimiento '
        sql += 'FROM Artista '
        sql += 'WHERE titulo = ?'
        self.__cursor.execute(sql, (self.__name,))
        row = self.__cursor.fetchone()
        self.__name = row[0]    # Investigar cómo utilizar claves textuales
        self.__country = row[1]
        self.__birthdate = row[2]

    def getId(self):
        return self.__id
