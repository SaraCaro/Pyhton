import sqlite3

class Disco:
    '''
    Representa a un disco perteneciente a un artista musical
    '''
    def __init__(self,connection,id=None,titulo=None,fecha=None,editor=None):
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__id = id
        self.__titulo = titulo
        self.__fecha = fecha
        self.__editor = editor
    
    def __str__(self):
        return f'{self.__titulo} es del editor {self.__editor} y fue sacado el {self.__fecha}'
    
    def save(self):
        '''
        Añadir un nuevo disco a la base de datos
        '''
        sql = 'INSERT INTO Disco (id, editor, fecha,titulo) VALUES (?, ?, ?,?)'
        
        self.__cursor.execute(sql, (self.__id, self.__editor, self.__fecha,self.__titulo))
        self.__connection.commit()

    
    def getId(self):
        return self.__id
    
    def getTitulo(self):
        return self.__titulo
    
    def getFecha(self):
        return self.__fecha

    def getEditor(self):
        return self.__editor
    
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
        sql = 'UPDATE Disco SET titulo = ?, fecha = ?, editor = ? WHERE id = ?'

        self.__cursor.execute(sql, (self.__titulo, self.__fecha, self.__editor, self.__id,))
        self.__connection.commit()
    
    def load(self):
        '''
        Carga en memoria un disco de la base de datos
        '''
        sql = 'SELECT titulo,fecha,editor FROM Disco WHERE id = ?'

        self.__cursor.execute(sql, (self.__id,))
        self.__cursor.execute(sql,(self.__id,))
        row = self.__cursor.fetchone()
        self.__titulo = row[0]
        self.__fecha = row[1]
        self.__editor = row[2]
    

myConnection = sqlite3.connect('./canciones.db')

# disco1 = Disco(myConnection,None,'Quincy John','23-01-1984','Thriller')

# disco1.save()
# print(disco1.load())