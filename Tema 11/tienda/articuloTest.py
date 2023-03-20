import sqlite3
import unittest
from main import Articulo

class ArticuloTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()
        cls.cur.execute('''CREATE TABLE articulo(
            codigo int primary key,
            denominacion text,
            precio float
            
        )''')
        cls.cur.execute("INSERT INTO articulo VALUES(123,'ropa',10.99)")

    @classmethod
    def TearDownClass(cls):
        cls.cur.execute('DROP TABLE Articulo')
        cls.connection.close()
    
    def test_constructor_AllParams_OK(self):
        # Given
        codigo = 12
        denominacion = 'Juguete'
        precio = 12.34
        # When
        myArticle = Articulo(ArticuloTest.connection, codigo, denominacion, precio)
        # Then
        self.assertIsNotNone(myArticle)
        self.assertIsInstance(myArticle, Articulo)
    
    def test_setterAndGetter_OK(self):
        # Given
        codigo = 12
        denominacion = 'Juguete'
        precio = 12.34
        myArticle = Articulo(self.connection,codigo)
        self.assertIsNotNone(myArticle)
        self.assertIsInstance(myArticle, Articulo)
        # When
        myArticle.setDenominacion(denominacion)
        myArticle.setPrecio(precio)
        # Then
        self.assertEqual(myArticle.getDenominacion(),denominacion)
        self.assertEqual(myArticle.getPrecio(),precio)
        self.assertEqual(myArticle.getCodigo(),codigo)
    
    def test_Save_OK(self):
        # Given
        codigo = 12
        denominacion = 'Juguete'
        precio = 12.34
        myArticle = Articulo(self.connection, codigo, denominacion, precio)
        # When
        myArticle.save()
        # Then
        self.cur.execute('SELECT codigo, denominacion, precio FROM articulo WHERE codigo = ?', (codigo,))
        result = self.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['codigo'], codigo)
        self.assertEqual(result['denominacion'], denominacion)
        self.assertEqual(result['precio'], precio)
        self.cur.execute('DELETE FROM articulo WHERE codigo = ?',(codigo,))
    
    @unittest.expectedFailure
    def test_Save_Fail(self):
        # Given
        codigo = 123
        denominacion = 'Juguete'
        precio = 12.34
        myArticle = Articulo(self.connection, codigo, denominacion, precio)
        # When
        myArticle.save()
    
    def test_Delete_OK(self):
        # Given
        codigo = 333
        codigo2 = 123
        denominacion = 'Juguete'
        precio = 12.34
        myArticle = Articulo(self.connection, codigo, denominacion, precio)
        self.cur.execute('INSERT INTO articulo(codigo,denominacion,precio) VALUES (?,?,?)',(codigo,denominacion,precio,))
        # When
        myArticle.delete()
        # Then
        self.cur.execute('SELECT codigo FROM articulo WHERE codigo = ?', (codigo,))
        result = self.cur.fetchall()
        self.assertEqual(result,[])
        self.cur.execute('SELECT denominacion FROM articulo WHERE denominacion = ?', (denominacion,))
        self.assertEqual(result,[])
        self.cur.execute('SELECT precio FROM articulo WHERE precio = ?', (precio,))
        self.assertEqual(result,[])
        self.cur.execute('DELETE FROM articulo WHERE codigo = ?',(codigo,))
        self.cur.execute('SELECT codigo FROM articulo WHERE codigo = ?', (codigo2,))
        result = self.cur.fetchall()
        self.assertNotEqual(result,[])
    
    def test_update(self):
        # Given
        codigo = 123
        denominacion = 'Juguete'
        precio = 12.34
        myArticle = Articulo(self.connection, codigo)
        self.cur.execute('SELECT codigo,denominacion, precio FROM articulo WHERE codigo = ?',(codigo,))
        original_values = self.cur.fetchone()
        # When
        myArticle.setDenominacion(denominacion)
        myArticle.setPrecio(precio)
        myArticle.update()
        # Then
        self.cur.execute('SELECT codigo,denominacion,precio FROM articulo WHERE codigo = ?', (codigo,))
        new_values = self.cur.fetchone()
        self.assertNotEqual(new_values,original_values)
        self.assertEqual(new_values['codigo'],codigo)
        self.assertEqual(new_values['denominacion'],denominacion)
        self.assertEqual(new_values['precio'],precio)
        # When2
        myArticle.setDenominacion(original_values['denominacion'])
        myArticle.setPrecio(original_values['precio'])
        myArticle.update()
        # Then2
        self.cur.execute('SELECT codigo,denominacion,precio FROM articulo WHERE codigo = ?', (codigo,))
        new_values = self.cur.fetchone()
        self.assertEqual(new_values,original_values)

    def test_load_OK(self):
        # Given
        self.cur.execute('SELECT codigo,denominacion, precio FROM articulo')
        article = self.cur.fetchone()
        codigo = article['codigo']
        myArticle = Articulo(self.connection, codigo)
        

        # When
        myArticle.load()
        # Then
        self.assertEqual(myArticle.getCodigo(),article['codigo'])
        self.assertEqual(myArticle.getDenominacion(),article['denominacion'])
        self.assertEqual(myArticle.getPrecio(),article['precio'])
    
    @unittest.expectedFailure
    def test_load_fail(self):
        # Given
        codigo = 444
        myArticle = Articulo(self.connection, codigo)

        # When
        myArticle.load()
        



if __name__ == '__main__':
    unittest.main()