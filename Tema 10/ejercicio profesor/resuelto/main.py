import sqlite3

class Cliente:
    '''
    Representa a un cliente de la tienda.
    '''

    def __init__(self, connection, dni, nombre=None, apellidos=None):
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos


    def setNombre(self, nuevoNombre):
        '''
        Cambia el atributo nombre por un nuevo nombre
        '''
        self.__nombre = nuevoNombre


    def save(self):
        '''
        Añadir un nuevo cliente a la base de datos
        '''
        sql = 'INSERT INTO cliente (dni, nombre, apellidos) VALUES (?, ?, ?)'
        
        self.__cursor.execute(sql, (self.__dni, self.__nombre, self.__apellidos))
        self.__connection.commit()


    def delete(self):
        '''
        Borra un cliente existente en la base de datos.
        '''
        sql = 'DELETE FROM cliente WHERE dni = ?'

        self.__cursor.execute(sql, (self.__dni,))
        self.__connection.commit()
    

    def update(self):
        '''
        Actualiza los datos de un cliente existente en la base de datos.
        '''
        sql = 'UPDATE cliente SET nombre = ?, apellidos = ? WHERE dni = ?'

        self.__cursor.execute(sql, (self.__nombre, self.__apellidos, self.__dni))
        self.__connection.commit()
    

    def load(self):
        '''
        Carga los datos de un cliente en memoria.
        '''
        sql = 'SELECT nombre, apellidos FROM cliente WHERE dni = ?'

        self.__cursor.execute(sql, (self.__dni,))
        row = self.__cursor.fetchone()
        self.__nombre = row[0]
        self.__apellidos = row[1]
    
    def getDni(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getApellidos(self):
        return self.__apellidos


class Articulo:
    '''
    Representa un artículo de la tienda
    '''

    def __init__(self, connection, codigo, denominacion=None, precio=None):
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__codigo = codigo
        self.__denominacion = denominacion
        self.__precio = precio

    def save(self):
        '''
        Añadir un nuevo articulo a la base de datos
        '''
        sql = 'INSERT INTO articulo (codigo, denominacion, precio) VALUES (?, ?, ?)'
        
        self.__cursor.execute(sql, (self.__codigo, self.__denominacion, self.__precio))
        self.__connection.commit()

    def delete(self):
        '''
        Borra un articulo existente en la base de datos.
        '''
        sql = 'DELETE FROM articulo WHERE codigo = ?'

        self.__cursor.execute(sql, (self.__codigo,))
        self.__connection.commit()

    def update(self):
        '''
        Actualiza los datos de un artículo existente en la base de datos.
        '''
        sql = 'UPDATE articulo SET denominacion = ?, precio = ? WHERE codigo = ?'

        self.__cursor.execute(sql, (self.__denominacion, self.__precio, self.__codigo))
        self.__connection.commit()
    
    def load(self):
        '''
        Carga los datos de un articulo en memoria.
        '''
        sql = 'SELECT denominacion, precio FROM articulo WHERE codigo = ?'

        self.__cursor.execute(sql, (self.__codigo,))
        row = self.__cursor.fetchone()
        self.__denominacion = row[0]
        self.__precio = row[1]

    def getDenominacion(self):
        return self.__denominacion
    
    def getPrecio(self):
        return self.__precio
    
    def getCodigo(self):
        return self.__codigo





class Factura:
    '''
    Representa una factura generada por un cliente de la tienda
    '''

    def __init__(self, connection, numero, cliente=None, direccion=None, fecha=None):
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__numero = numero
        self.__cliente = cliente
        self.__direccion = direccion
        self.__fecha = fecha
        self.__listaLineas = []


    def addLine(self, linea):
        '''
        Añade lineas al atributo listaLineas.
        La línea debe estar ya en la base de datos
        linea = objeto de la clase línea
        '''
        self.__listaLineas.append(linea)


    def deleteLineas(self, indice):
        '''
        Borra lineas de la lista de lineas
        indice = int. Es el índice de la línea que queremos borrar
                de la base de datos
        '''
        self.__listaLineas[indice].delete()
        del self.__listaLineas[indice]


    def calculateTotalPrice(self):
        '''
        Calcula el precio total en una factura del atributo
        lineas

        return total float
        '''
        total = 0
        for linea in self.__listaLineas:
            total += linea.calculatePrice()
        return total

    def save(self):
        '''
        Añadir una nueva factura a la base de datos
        '''
        sql = 'INSERT INTO factura (numero, dni_cliente, direccion, fecha) VALUES (?, ?, ?, ?)'
        
        self.__cursor.execute(sql, (self.__numero, self.__cliente.getDni(), self.__direccion, self.__fecha))
        self.__connection.commit()

    def delete(self):
        '''
        Borra una factura existente en la base de datos.
        '''
        sql = 'DELETE FROM factura WHERE numero = ?'

        self.__cursor.execute(sql, (self.__numero,))
        self.__connection.commit()

    def update(self):
        '''
        Actualiza los datos de una factura existente en la base de datos.
        '''
        sql = 'UPDATE factura SET dni_cliente = ?, direccion = ?, fecha = ? WHERE numero = ?'

        self.__cursor.execute(sql, (self.__cliente.getDni(), self.__direccion, self.__fecha, self.__numero))
        self.__connection.commit()
    
    def load(self):
        '''
        Carga los datos de una factura en memoria.
        '''
        sql = 'SELECT dni_cliente, direccion, fecha FROM factura WHERE numero = ?'

        self.__cursor.execute(sql, (self.__numero,))
        row = self.__cursor.fetchone()
        miCliente = Cliente(self.__connection, row[0])
        miCliente.load()
        self.__cliente = miCliente
        self.__direccion = row[1]
        self.__fecha = row[2]
        self.loadLines()

    def getNumero(self):
        return self.__numero

    def getLines(self):
        return self.__listaLineas

    def loadLines(self):
        '''
        Carga en memoria las líneas existentes
        en una factura de la base de datos
        '''
        sql = 'SELECT numero_linea, articulo, cantidad FROM linea WHERE numero_factura = ?'

        self.__cursor.execute(sql, (self.__numero,))
        rows = self.__cursor.fetchall()
        for row in rows:
            articulo = Articulo(self.__connection, row[1])
            articulo.load()
            linea = Linea(self.__connection, row[0], self, articulo, row[2])
            self.__listaLineas.append(linea)

class Linea:
    '''
    Representa una línea en una factura.
    '''

    def __init__(self, connection, numLinea, factura, articulo=None, cantidad=None):
        self.__connection = connection
        self.__cursor = connection.cursor()
        self.__articulo = articulo
        self.__cantidad = cantidad
        self.__factura = factura
        self.__numero = numLinea
    
    def save(self):
        '''
        Añadir una nueva línea de una factura a la base de datos.
        '''
        sql = 'INSERT INTO linea (numero_factura, numero_linea, articulo, cantidad) VALUES (?, ?, ?, ?)'
        
        values = (
            self.__factura.getNumero(),
            self.__numero,
            self.__articulo.getCodigo(),
            self.__cantidad,
        )

        self.__cursor.execute(sql, values)
        self.__connection.commit()

    def delete(self):
        '''
        Borra una línea de una factura existente en la base de datos.
        '''
        sql = 'DELETE FROM linea WHERE numero_factura = ? AND numero_linea = ?'

        self.__cursor.execute(sql, (self.__factura.getNumero(), self.__numero))
        self.__connection.commit()

    def update(self):
        '''
        Actualiza los datos de una linea en una factura existente en la base de datos.
        '''
        sql = 'UPDATE linea SET articulo = ?, cantidad = ? WHERE numero_factura = ? AND numero_linea = ?'

        values = (
            self.__articulo.getCodigo(),
            self.__cantidad,
            self.__factura.getNumero(),
            self.__numero,
        )
        self.__cursor.execute(sql, values)
        self.__connection.commit()
    
    def load(self):
        '''
        Carga los datos de una linea en una factura en memoria.
        '''
        sql = 'SELECT articulo, cantidad FROM linea WHERE numero_factura = ? AND numero_linea = ?'

        values = (
            self.__factura.getNumero(),
            self.__numero,
        )
        self.__cursor.execute(sql, values)
        row = self.__cursor.fetchone()
        miArticulo = Articulo(self.__connection, row[0])
        miArticulo.load()
        self.__articulo = miArticulo
        self.__cantidad = row[1]
    
    def getNumero(self):
        return self.__numero

    def getFactura(self):
        return self.__factura

    def calculatePrice(self):
        '''
        Calcula el precio total existente en una línea.
        Resultado = valor total (float)
        '''
        return self.__articulo.getPrecio() * self.__cantidad

myConnection = sqlite3.connect('database.db')

# cliente = Cliente('53912889s', 'Juan', 'Marquez')
# articulo = Articulo(12, 'Pela patatas', 9)
# factura = Factura(1, cliente)
# linea = Lineas(articulo, 2)
# linea2 = Lineas(articulo, 9)
# factura.addLineas(linea)
# factura.addLineas(linea2)
# result = factura.calculateTotalPrice()

# cliente2 = Cliente('31213312', 'Paco', 'IIIII')

# factura.modificarBaseDeDatos(cliente2)
