import sys
import os
sys.path.append(os.path.abspath('.'))

import sqlite3
import unittest
from sport import Sport


class SportTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()
        cls.cur.execute('''CREATE TABLE sports(
            id int primary key,
            name text,
            vacances float,
            trainer int
        )''')

        cls.cur.execute('''CREATE TABLE trainers(
            id int primary key,
            nombre text,
            phone int
        )''')
        cls.cur.execute("INSERT INTO trainers VALUES(2,'Belen',672910488)")

    @classmethod
    def TearDownClass(cls):
        cls.cur.execute('DROP TABLE sports')
        cls.connection.close()
    
    def test_constructor_AllParams_OK(self):
        # Given
        id = 1
        name = 'Futbol'
        vacances = 10
        trainer = 3
        # When
        mySport = Sport(SportTest.connection, id, name, vacances, trainer)
        # Then
        self.assertIsNotNone(mySport)
        self.assertIsInstance(mySport, Sport)
    
    def test_load_OK(self):
        # Given
        id = 1
        name = 'Futbol'
        vacances = 10
        trainer = 3
        mySport = Sport(self.connection, id, name, vacances, trainer)
        self.cur.execute('INSERT INTO sports(id,name,vacances,trainer) VALUES (?,?,?,?)',(id,name,vacances,trainer,))

        # When
        mySport.load()
        # Then
        self.cur.execute('SELECT id, name, vacances, trainer FROM sports')
        sport = self.cur.fetchone()
        self.assertEqual(id,sport['id'])
        self.assertEqual(vacances,sport['vacances'])
    
if __name__ == '__main__':
    unittest.main()