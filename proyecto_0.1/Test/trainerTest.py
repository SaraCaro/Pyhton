import sys
import os
sys.path.append(os.path.abspath('.'))

import sqlite3
import unittest
from trainers import Trainers


class TrainerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()

        cls.cur.execute('''CREATE TABLE trainers(
            id int primary key,
            nombre text,
            phone int
        )''')
        cls.cur.execute("INSERT INTO trainers VALUES(2,'Belen',672910488)")

    @classmethod
    def TearDownClass(cls):
        cls.cur.execute('DROP TABLE trainers')
        cls.connection.close()
    
    def test_constructor_AllParams_OK(self):
        # Given
        id = 2
        nombre = 'Belen'
        phone = 628104729
        # When
        myTrainer = Trainers(TrainerTest.connection, id, nombre, phone)
        # Then
        self.assertIsNotNone(myTrainer)
        self.assertIsInstance(myTrainer, Trainers)
    
    def test_load_OK(self):
        # Given
        self.cur.execute('SELECT id,nombre, phone FROM trainers')
        trainer = self.cur.fetchone()
        codigo = trainer['id']
        myTrainer = Trainers(self.connection, codigo)
        
        # When
        myTrainer.load()
        # Then
        self.assertEqual(myTrainer.getID(),trainer['id'])
    
    @unittest.expectedFailure
    def test_load_fail(self):
        # Given
        id = 'Tenis'
        myTrainer = Trainers(self.connection, id)

        # When
        myTrainer.load()
        
if __name__ == '__main__':
    unittest.main()