from contact_scm import Contact

class Quotes:
    '''
    Representa las citas de los contactos
    '''

    def __init__(self, connection, id=None, contacts=[None], description=None, place=None, date=None, hour=None):
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__id = id
        self.__contacts = contacts
        self.__description = description
        self.__place = place
        self.__date = date
        self.__hour = hour


    def __str__(self):
        result = f'\nEl ID es: {self.__id} '
        if self.__contacts is not None:
            result += f' \nContacto: {self.__contacts.getName()}'
        if self.__description is not None:
            result += f' \nDescripción: {self.__description}'
        if self.__place is not None:
            result += f' \nLugar: {self.__place}'
        if self.__date is not None:
            result += f' \nDia: {self.__date}'
        if self.__hour is not None:
            result += f' \nHora: {self.__hour}\n'
        return result


    def save(self):
        '''
        Añade una nueva cita a la base de datos.
        '''
        sql = 'INSERT INTO Quotes (id, contacts, description, place, date, hour) '
        sql += 'VALUES (?, ?, ?, ?, ?, ?)'
        myContact = self.__contacts.getId() if self.__contacts.getId() is not None else None
        values = (
            self.__id,
            myContact,
            self.__description,
            self.__place,
            self.__date,
            self.__hour,
        )
        self.__cursor.execute(sql, values)
        self.__connection.commit()


    def delete(self):
        '''
        Borra una cita existente en la base de datos.
        '''
        sql = 'DELETE FROM Quotes WHERE id = ?'
        self.__cursor.execute(sql, (self.__id,))
        self.__connection.commit()
    


    def update(self):
        '''
        Actualiza los datos de una cita existente en la base de datos.
        '''
        sql = 'UPDATE Quotes SET  contacts = ?, description = ?, place = ?, date = ?, hour = ? '
        sql += 'WHERE id = ?'
        values = (
            self.__id,
            self.__contacts,
            self.__description,
            self.__place,
            self.__date,
            self.__hour,
        )
        self.__cursor.execute(sql, values)
        self.__connection.commit()
    


    def load(self):
        '''
        Carga en memoria una cita de la base de datos.
        '''
        if self.__id is None:
            raise TypeError('El atributo id debe tener valor')
        sql = 'SELECT contacts, description, place, date, hour '
        sql += 'name, surname, email, phone, address '
        sql += 'FROM Quotes '
        sql += 'LEFT JOIN Contact ON Contact.id = Quotes.contacts '
        sql += 'WHERE Quotes.id = ?'
        self.__cursor.execute(sql, (self.__id,))
        row = self.__cursor.fetchone()
        self.__contacts = row[0] 
        self.__description = row[1] 
        self.__place = row[2] 
        self.__date = row[3] 
        self.__hour = row[4] 
        if row[5] is not None:
            self.__contacts = Contact(self.__connection, row[4], row[6], row[7], row[8])
    

    def saveQuote_Contacts(self):
        '''
        Guarda en la tabla Has la relación entre Quote
        y Contacts
        '''
        if self.__id is None:
            raise TypeError('El id debe tener valor')
        if self.__contacts == [None]:
            raise TypeError('El contacts debe tener valor')
        sql = 'INSERT INTO has (contact_id, '
        sql += 'quotes_id) VALUES (?, ?)'
        for contacts in self.__contacts:
            self.__cursor.execute(sql,(contacts.getId(), self.__id,))
        self.__connection.commit()