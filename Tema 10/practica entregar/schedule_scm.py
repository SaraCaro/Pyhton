import sqlite3
from unittest import result
from contact_scm import Contact
from quote_scm import Quotes

class ScheduleManager:
    '''Gestiona los objetos de la clase Contact y Quote en la base de datos'''

    def __init__(self,connection):
        self.__connection = connection
        self.__connection.row_factory = sqlite3.Row
        self.__cursor = connection.cursor()
    
    def loadByFile(self,archive):
        '''
        Extraer los datos de un archivo de entrada
        
        archive = nombre del archivo (str)
        '''
        with open(archive,encoding='utf-8') as archive:
            strip_lines = [line.strip() for line in archive]
            content_line = [line for line in strip_lines if line]
            result = set()
            for line in content_line:
                data = line.split(",")
                space_data = [value.strip() for value in data]
                for i in range(len(space_data)):
                    if space_data[i] == '':
                        space_data[i] = None
                extractContact = Contact(
                    self.__connection,
                    None,
                    space_data[0],
                    space_data[1],
                    space_data[2],
                    space_data[3],
                    space_data[4],
                )
                result.add(extractContact)
            return result

# Obtener datos de Contacto
    
    def getByIdsContact(self,*ids):
        '''
        Devuelve colección de objetos de tipo Contact

        ids = coleccion de ids correspondientes a contactos en la base datos 
        resultado = (set) objetos de la clase Contact
        '''
        sql = 'SELECT Contact.id AS c_id,  name,surname,email,phone,address '
        sql += 'FROM Contact '
        if len(ids) > 1:
            sql += 'WHERE Contact.id IN {}'.format(ids)
        else:
            sql += 'WHERE Contact.id == {}'.format(ids[0])
        self.__cursor.execute(sql)
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myContact = Contact(self.__connection, row[0], row[1], row[2], row[3], row[4], row[5])
            result.add(myContact)
        return result


    def __getByBaseContact(self, key, value):
        '''
        Método base para buscar en contactos por alguna de sus
        columnas.

        key = la columna por la que busco
        value = el valor o parte de ello
        result = lista de contactos
        '''
        sql = 'SELECT id, name, surname, email, phone, address '
        sql += 'FROM Contact '
        sql += 'WHERE lower({}) LIKE lower(?)'.format(key)
        self.__cursor.execute(sql, (f'%{value}%',))
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            mycontact = Contact(self.__connection, row[0], row[1], row[2], row[3])
            result.add(mycontact)
        return result

    def getByNameContact(self,name):
        return self.__getByBaseContact('name', name)
        
    def getByTelephoneContact(self, phone):
        return self.__getByBaseContact('phone', phone)
        
    def getByAddressContact(self, address):
        return self.__getByBaseContact('address', address)
        
    def getByEmailContact(self, email):
        return self.__getByBaseContact('email', email)

    
        
# Obtener datos de Citas
    def getByIdsQuote(self,*ids):
        '''
        Devuelve colección de objetos de tipo Quote

        ids = coleccion de ids correspondientes a contactos en la base datos 
        resultado = (set) objetos de la clase Quote
        '''
        sql = 'SELECT id AS q_id,  id,contacts,place,date,hour '
        sql += 'FROM Quotes '
        sql += 'WHERE Quotes.id IN {}'.format(ids)
        self.__cursor.execute(sql)
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            contact = self.getByIdsContact(row[1])
            myCite = Quotes(self.__connection, row[0], list(contact)[0], row[2], row[3], row[4], row[5])
            result.add(myCite)
        return result

    def __getByBaseQuote(self, key, value):
        '''
        Método base para buscar en citas por alguna de sus
        columnas.

        key = la columna por la que busco
        value = el valor o parte de ello
        result = lista de citas
        '''
        sql = 'SELECT id,contacts,place,date,hour '
        sql += 'FROM Quotes '
        sql += 'WHERE lower({}) LIKE lower(?)'.format(key)
        self.__cursor.execute(sql, (f'%{value}%',))
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            contact = self.getByIdsContact(row[1])
            myCite = Quotes(self.__connection, row[0], list(contact)[0], row[4], row[2], row[3])
            result.add(myCite)
        return result

    def getByDateQuote(self,date):
        return self.__getByBaseQuote('date', date)
        
    def getByPlaceQuote(self, place):
        return self.__getByBaseQuote('place', place)
    
    def getByContactsQuote(self, myContact):
        '''
        Devuelve colección de objetos de tipo Quote

        myContact = los contactos de la cita
        resultado = (set) objetos de la clase Quote
        '''
        sql = 'SELECT id, description, place, '
        sql += 'date, hour '
        sql += 'FROM Quotes '
        sql += 'LEFT JOIN has ON has.quotes_id = Quotes.id '
        sql += 'WHERE contact_id = ?'
        self.__cursor.execute(sql, (f'%{myContact}%',),)
        rows = self.__cursor.fetchall()
        result = set()
        for row in rows:
            myCite = Quotes(self.__connection, row[0], row[1], row[2], row[3], row[4])
            result.add(myCite)
        return result
    
