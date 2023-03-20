class Contact:
    '''
    Representa un contacto
    '''
  
    def __init__(self, connection, id=None, name=None, surname=None, email=None, phone=None, address=None):
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__id = id 
        self.__name = name
        self.__surname = surname
        self.__email = email
        self.__phone = phone
        self.__address = address


    def __str__(self):
        # return f'\nEl contacto con id {self.__id} y nombre = {self.__name}'
        result = f'El ID es: {self.__id} '
        if self.__name is not None:
            result += f' \nNombre: {self.__name}'
        if self.__surname is not None:
            result += f' \nApellidos: {self.__surname}'
        if self.__email is not None:
            result += f' \nEmail: {self.__email}'
        if self.__phone is not None:
            result += f' \nNumero: {self.__phone}'
        if self.__address is not None:
            result += f' \nDireccion: {self.__address}\n'
        return result


    def save(self):
        '''
        Añade un nuevo contacto a la base de datos.
        '''
        sql = 'INSERT INTO Contact (id, name, surname, email, phone, address) '
        sql += 'VALUES (?, ?, ?, ?, ?, ?)'
        values = (
            self.__id,
            self.__name,
            self.__surname,
            self.__email,
            self.__phone,
            self.__address,
        )
        self.__cursor.execute(sql, values)
        self.__connection.commit()


    def getId(self):
        return self.__id


    def getName(self):
        return self.__name
    

    def getSurname(self):
        return self.__surname
    


    def delete(self):
        '''
        Borra un contacto existente en la base de datos.
        '''
        sql = 'DELETE FROM Contact WHERE id = ?'
        self.__cursor.execute(sql, (self.__id,))
        self.__connection.commit()
    

    def update(self):
        '''
        Actualiza los datos de un contacto existente en la base de datos.
        '''
        sql = 'UPDATE Contact SET name = ?, surname = ?, email = ?, phone = ?, address = ? '
        sql += 'WHERE id = ?'
        values = (
            self.__name,
            self.__surname,
            self.__email,
            self.__phone,
            self.__address,
            self.__id,
        )
        self.__cursor.execute(sql, values)
        self.__connection.commit()
    


    def load(self):
        '''
        Carga en memoria un contacto de la base de datos.
        '''
        if self.__id is None:
            raise TypeError('El atributo id debe tener valor')
        sql = 'SELECT name,surname,email,phone,address '
        sql += 'FROM Contact '
        sql += 'WHERE id = ?'
        self.__cursor.execute(sql, (self.__id,))
        row = self.__cursor.fetchone()
        self.__name = row[0]
        self.__surname = row[1] 
        self.__email = row[2]
        self.__phone = row[3]
        self.__address = row[4]