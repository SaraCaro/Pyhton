from multiprocessing.connection import Client
import sqlite3

conn = sqlite3.connect("./ejercicio.db")
cur = conn.cursor()

class Customers:
    '''Representa a clientes'''
    def __init__(self,dni,name=None,surname = None):
        self.dni = dni
        self.name = name
        self.surname = surname
    
    def __str__(self):
        return f'La persona con DNI: {self.dni} se llama {self.name} {self.surname}'
    
    def insertCustomer(self):
        '''Añadir nuevo cliente a Base de datos'''
        cur.execute("INSERT INTO Customers (dni,name,surname) VALUES (?,?,?)",(self.dni,self.name,self.surname))
    
    def getCustomer(self):
        '''Carga los datos de un cliente en memoria'''
        cur.execute('SELECT dni,name,surname FROM Customers')
    
    def updateCustomer(self,newName,newSurname):
        cur.execute('UPDATE Customers SET name = ?, surname = ? WHERE dni = ?',(newName,newSurname,self.dni))


class Article:
    '''Representa articles'''
    def __init__(self,id,denomination,price):
        self.id = id
        self.denomination = denomination
        self.price = price
    
    def __str__(self):
        return f'El id es: {self.id}, denomination: {self.denomination} y price: {self.price}'
    
    def insertArticle(self):
        '''Añadir Articulo a la Base de Datos'''
        cur.execute("INSERT INTO Article (id,denomination,price) VALUES (?,?,?)",(self.id,self.denomination,self.price))
        
    def updateCustomer(self):
        cur.execute('UPDATE Article SET denomination = ?, precio = ? WHERE codigo = ?',(self.denomination,self.id,self.price))

    def getCustomer(self):
        '''Carga los datos de un cliente en memoria'''
        cur.execute('SELECT id,denomination,price FROM Article')

class Invoice:
    '''Representa facturas'''
    def __init__(self,number,customer,direccion,date):
        self.number = number
        self.customer = customer
        self.direccion = direccion
        self.date = date
    
    def __str__(self):
        return f'Factura {self.number} del customers {self.customer}'
    
    def insertArticle(self):
        '''Añadir Factura a la Base de Datos'''
        cur.execute("INSERT INTO Factura (number,customers,direccion,date) VALUES (?,?,?,?)",(self.number,self.customer,self.direccion,self.date))
    
    def TotalPrice(self):
        total = 0
        for lines in self.lines:
            total += lines.subtotal

class InvoiceLine:
    '''Representa las lines'''
    def __init__(self,article,amount,price):
        self.article = article
        self.amount = amount
        self.price = price
    
    def subTotal(self):
        subtotal = self.price * self.amount
        return subtotal

    def insertInvoiceLine(self):
        cur.execute("INSERT INTO InvoiceLine (article,amount) VALUES (?,?,?)",(self.article,self.amount,self.subTotal()))


# persona = Customers(22342, "Pepe", "Juan")
# persona.insertCustomer()

# persona2 = Customers(89053, "Pedro", "Espigares")
# persona2.insertCustomer()

# art1 = Article(3,"España", 5.5)
# linea1 = InvoiceLine(art1, 2)
# print("Precio línea 1: ", linea1.subTotal(), "€")
# art1.insertArticle()

# art2 = Article(5,"Portugal", 7)
# linea2 = InvoiceLine(art2, 4)
# print("Precio línea 2: ", linea2.subTotal(), "€")
# art2.insertArticle()

# lineas = (linea1, linea2)
# factura = Invoice(1, persona, lineas)
# # print("Precio total de la factura: ", factura.TotalPrice(), "€")

linea1 = InvoiceLine(3,115,3.5)
linea1.insertInvoiceLine()

conn.commit()