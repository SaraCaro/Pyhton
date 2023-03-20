import sqlite3

class Cancion:
    def __init__(self,connection,id,titulo_ca=None,duracion=None,genero=None,contenido=None):
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__id = id
        self.__titulo_ca = titulo_ca
        self.__duracion = duracion
        self.__genero = genero
        self.__contenido = contenido
    
    def __str__(self):
        return f'{self.__titulo_ca} dura {self.__duracion} con género de {self.__genero} y tiene el contenido {self.__contenido}'
    
    def save(self):
        '''
        Añadir un nuevo Cancion a la base de datos
        '''
        sql = 'INSERT INTO Cancion (id, titulo_ca, duracion,genero,contenido) VALUES (?, ?, ?,?)'
        
        self.__cursor.execute(sql, (self.__id, self.__duracion, self.__genero,self.__contenido))
        self.__connection.commit()

    
    def getId(self):
        return self.__id
    
    def getTitulo(self):
        return self.__titulo_ca
    
    def getDuracion(self):
        return self.__duracion

    def getGenero(self):
        return self.__genero
    
    def getContenido(self):
        return self.__contenido
    
    def load(self):
        '''
        Carga los datos de una cancion
        '''
        sql = 'SELECT id, titulo_ca, duracion, genero, contenido FROM Cancion WHERE id = ? AND genero = ?'

        values = (
            self.__id
        )
        self.__cursor.execute(sql, values)
        row = self.__cursor.fetchone()
        miCancion = Cancion(self.__connection, row[0])
        miCancion.load()
        miCancion.__titulo_ca = row[1]
        miCancion.__duracion = row[2]
        miCancion.__genero = row[3]
        miCancion.__contenido = row[4]
    

myConnection = sqlite3.connect('./canciones.db')
