import sqlite3
import unittest
from main import Cliente

class ClienteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()
        cls.cur.execute('''CREATE TABLE Cliente(
            dni int primary key,
            nombre text,
            apellidos text
            )
        ''')

    @classmethod
    def TearDownClass(cls):
        cls.cur.execute('DROP TABLE Articulo')
        cls.connection.close()

    def test_constructor_AllParams_OK(self):
        # Given
        dni = '12345675G'
        nombre = 'Alvaro'
        apellidos = 'Fernandez'
        # When
        myClient = Cliente(ClienteTest.connection, dni, nombre, apellidos)
        # Then
        self.assertIsNotNone(myClient)
        self.assertIsInstance(myClient, Cliente)
    
    def test_constructor_OnlyObligatoryParam_OK(self):
        # Given
        dni = '123456754G'
        # When
        myClient = Cliente(ClienteTest.connection, dni)
        # Then
        self.assertIsNotNone(myClient)
        self.assertIsInstance(myClient, Cliente)
    
    def test_setterAndGetter_Nombre_OK(self):
        # Given
        dni = '123456754G'
        nombre = 'Alvaro'
        apellidos = 'Fernandez'
        # When
        myClient = Cliente(ClienteTest.connection, dni)
        myClient.setNombre(nombre)
        myClient.setApellido(apellidos)
        # Then
        self.assertEqual(myClient.getNombre(),nombre)
        self.assertEqual(myClient.getApellidos(),apellidos)
        self.assertEqual(myClient.getDni(),dni)
    
    def test_Save_OK(self):
        # Given
        dni = '12345675G'
        nombre = 'Alvaro'
        apellidos = 'Fernandez'
        myClient = Cliente(ClienteTest.connection, dni, nombre, apellidos)
        # When
        myClient.save()
        # Then
        ClienteTest.cur.execute('SELECT dni, nombre, apellidos FROM Cliente WHERE dni = ?', (dni,))
        result = ClienteTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['dni'], dni)
        self.assertEqual(result['nombre'], nombre)
        self.assertEqual(result['apellidos'], apellidos)
        self.cur.execute('DELETE FROM cliente WHERE dni = ?',(dni,))
    
    def test_SaveWithSetter_OK(self):
        # Given
        dni = '12345679G'
        nombre = 'Alvaro'
        apellidos = 'Fernandez'
        myClient = Cliente(ClienteTest.connection, dni)
        # When
        myClient.setNombre(nombre)
        myClient.setApellido(apellidos)
        myClient.save()
        # Then
        ClienteTest.cur.execute('SELECT dni, nombre, apellidos FROM Cliente WHERE dni = ?', (dni,))
        result = ClienteTest.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['dni'], dni)
        self.assertEqual(result['nombre'], nombre)
        self.assertEqual(result['apellidos'], apellidos)
        self.cur.execute('DELETE FROM cliente WHERE dni = ?',(dni,))
    
    def test_Delete_OK(self):
        # Given
        dni = '12345675G'
        nombre = 'Alvaro'
        apellidos = 'Fernandez'
        myClient = Cliente(ClienteTest.connection, dni)
        self.cur.execute('INSERT INTO Cliente(dni,nombre,apellidos) VALUES (?,?,?)',(dni,nombre,apellidos,))
        # When
        myClient.delete()
        # Then
        result = self.cur.fetchall()
        ClienteTest.cur.execute('SELECT dni FROM Cliente WHERE dni = ?', (dni,))
        self.assertEqual(result,[])
        ClienteTest.cur.execute('SELECT nombre FROM Cliente WHERE nombre = ?', (nombre,))
        self.assertEqual(result,[])
        ClienteTest.cur.execute('SELECT apellidos FROM Cliente WHERE apellidos = ?', (apellidos,))
        self.assertEqual(result,[])
        self.cur.execute('DELETE FROM cliente WHERE dni = ?',(dni,))
    
    def test_update(self):
        # Given
        dni = '12345675G'
        nombre1 = 'Alvaro'
        apellidos1 = 'Fernandez'
        nombre2 = 'Pepe'
        apellidos2 = 'Garcia'
        myClient = Cliente(ClienteTest.connection, dni)
        self.cur.execute('INSERT INTO Cliente(dni,nombre,apellidos) VALUES (?,?,?)',(dni,nombre1,apellidos1,))
        # When
        myClient.setNombre(nombre2)
        myClient.setApellido(apellidos2)
        myClient.update()
        # Then
        ClienteTest.cur.execute('SELECT dni,nombre,apellidos FROM Cliente WHERE dni = ?', (dni,))
        result = self.cur.fetchone()
        self.assertEqual(result['nombre'],nombre2)
        self.assertEqual(result['apellidos'],apellidos2)
        self.cur.execute('DELETE FROM cliente WHERE dni = ?',(dni,))
    
    def test_load(self):
        # Given
        dni = '12345675G'
        nombre = 'Alvaro'
        apellidos = 'Fernandez'
        myClient = Cliente(ClienteTest.connection, dni)
        self.cur.execute('INSERT INTO Cliente(dni,nombre,apellidos) VALUES (?,?,?)',(dni,nombre,apellidos,))
        # When
        myClient.load()
        # Then
        self.assertEqual(myClient.getNombre(),nombre)
        self.assertEqual(myClient.getApellidos(),apellidos)
        self.cur.execute('DELETE FROM cliente WHERE dni = ?',(dni,))


if __name__ == '__main__':
    unittest.main()