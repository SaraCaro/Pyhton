import sqlite3
import unittest
from main import Factura, Cliente, Linea, Articulo

class FacturaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()
        cls.cur.execute('''CREATE TABLE articulo(
            dni_cliente int primary key,
            direccion text,
            fecha float
        )''')
        cls.cur.execute("INSERT INTO articulo VALUES(123,'ropa',10.99)")
        cls.cur.execute("INSERT INTO articulo VALUES(738,'deporte',20.99)")

        cls.cur.execute('''CREATE TABLE cliente(
            dni int primary key,
            nombre text,
            apellidos text
        )''')
        cls.cur.execute("INSERT INTO cliente VALUES('77253819L','Alvaro','Perez')")

        cls.cur.execute('''CREATE TABLE factura(
            numero int primary key,
            dni_cliente int,
            direccion text,
            fecha date
        )''')
        cls.cur.execute("INSERT INTO factura VALUES(1,'77253819L','Calle Pedro Antonio','12/05/2022')")

        cls.cur.execute('''CREATE TABLE linea(
            articulo int,
            cantidad int,
            numero_factura int,
            numero_linea int,
            primary key(numero_factura, numero_linea)
        )''')
        cls.cur.execute("INSERT INTO linea VALUES(1,1,123,4)")
        cls.cur.execute("INSERT INTO linea VALUES(2,2,738,2)")
    
    @classmethod
    def TearDownClass(cls):
        cls.cur.execute('DROP TABLE articulo')
        cls.cur.execute('DROP TABLE cliente')
        cls.cur.execute('DROP TABLE factura')
        cls.cur.execute('DROP TABLE linea')
        cls.connection.close()
    
    def test_constructor_AllParams_OK(self):
        # Given
        numero = 2
        myCliente = Cliente(self.connection,'77253819L') 
        direccion = 'Calle Navas'
        fecha = '02/04/2011'
        # When
        myFacture = Factura(self.connection, numero, myCliente, direccion, fecha)
        # Then
        self.assertIsNotNone(myFacture)
        self.assertIsInstance(myFacture, Factura)
        self.assertEqual(myFacture.getDireccion(),direccion)
        self.assertEqual(myFacture.getFecha(),fecha)
        self.assertEqual(myFacture.getCliente(), myCliente)
    
    def test_setterAndGetter_OK(self):
       # Given
        numero = 2
        myCliente = Cliente(self.connection,'77253819L') 
        direccion = 'Calle Navas'
        fecha = '02/04/2012'
        myFacture = Factura(self.connection, numero)
        # When
        myFacture.setCliente(myCliente)
        myFacture.setDireccion(direccion)
        myFacture.setFecha(fecha)
        # Then
        self.assertEqual(myFacture.getDireccion(),direccion)
        self.assertEqual(myFacture.getFecha(),fecha)
        self.assertEqual(myFacture.getCliente(), myCliente)
    
    def test_load_OK(self):
        # Given
        self.cur.execute('SELECT numero,dni_cliente, direccion, fecha FROM factura')
        factura = self.cur.fetchone()
        numero = factura['numero']
        self.cur.execute('SELECT numero_linea FROM linea WHERE numero_factura = ?',(numero,))
        lineas = self.cur.fetchall()
        myFacture = Factura(self.connection, numero)
        # When
        myFacture.load()
        # Then
        self.assertEqual(myFacture.getNumero(),factura['numero'])
        self.assertEqual(myFacture.getCliente().getDni(),factura['dni_cliente'])
        self.assertEqual(myFacture.getFecha(),factura['fecha'])
        self.assertEqual(len(myFacture.getLines()),len(lineas))
    
    def test_Save_OK(self):
        # Given
        numero = 2
        myCliente = Cliente(self.connection,'77253819L') 
        direccion = 'Calle Navas'
        fecha = '02/04/2012'
        myFacture = Factura(self.connection, numero, myCliente, direccion, fecha)
        # When
        myFacture.save()
        # Then
        self.cur.execute('SELECT dni_cliente, direccion, fecha FROM factura WHERE numero = ?', (numero,))
        result = self.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['dni_cliente'], myCliente.getDni())
        self.assertEqual(result['direccion'], direccion)
        self.assertEqual(result['fecha'], fecha)
        self.cur.execute('DELETE FROM factura WHERE numero = ?',(numero,))
    
    def test_update_OK(self):
        # Given
        self.cur.execute('SELECT numero, dni_cliente, direccion, fecha FROM factura WHERE numero = 1')
        originalData = self.cur.fetchone()
        nuevaFecha = '2022/03/01'
        nuevaDireccion = 'Calle Recogidas'
        myClient = Cliente(self.connection, originalData['dni_cliente'])
        myFacture = Factura(self.connection, originalData['numero'], myClient, originalData['direccion'], originalData['fecha'])
        myClient2 = Cliente(self.connection, '12345678A')
        # When
        myFacture.setCliente(myClient2)
        myFacture.setFecha(nuevaFecha)
        myFacture.setDireccion(nuevaDireccion)
        myFacture.update()
        # Then
        self.cur.execute('SELECT numero, dni_cliente, direccion, fecha FROM factura WHERE numero = 1')
        result = self.cur.fetchone()
        self.assertEqual(nuevaDireccion,result['direccion'])
        self.assertEqual(nuevaFecha,result['fecha'])
        self.assertEqual(myClient2.getDni(),result['dni_cliente'])
        self.cur.execute('UPDATE factura SET direccion= ?, fecha = ?, dni_cliente = ? where numero = 1', 
        (originalData['direccion'], originalData['fecha'],originalData['dni_cliente']))
    
    def test_delete_OK(self):
        # Given
        self.cur.execute("INSERT INTO factura values(2, '87543232Z', 'Calle Gran via', 2022/8/6)")
        self.cur.execute("INSERT INTO linea VALUES(1,2,123,5)")
        self.cur.execute("INSERT INTO linea VALUES(2,2,324,9)")
        myFacture = Factura(self.connection,2)
        # When
        myFacture.delete()
        # Then
        self.cur.execute('SELECT numero FROM factura WHERE numero = 2')
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        self.cur.execute('SELECT numero_linea FROM linea WHERE numero_factura = 2')
        result = self.cur.fetchall()
        self.assertEqual(result, [])
    
    def test_deleteLineas_OK(self):
        # Given
        self.cur.execute("INSERT INTO factura values(2, '87543232Z', 'Calle Gran via', 2022/8/6)")
        self.cur.execute("INSERT INTO linea VALUES(1,2,123,5)")
        self.cur.execute("INSERT INTO linea VALUES(2,2,324,9)")
        myFacture = Factura(self.connection,2)
        # When
        myFacture.deleteLinea(0)
        myFacture.deleteLinea(1)
        # Then
        self.cur.execute('SELECT numero FROM factura WHERE numero = 2')
        result = self.cur.fetchall()
        self.assertNotEqual(result, [])
        self.cur.execute('SELECT numero_linea FROM linea WHERE numero_factura = 2')
        result = self.cur.fetchall()
        self.assertEqual(result, [])
        self.cur.execute('DELETE FROM factura WHERE numero = 2')


if __name__ == '__main__':
    unittest.main()