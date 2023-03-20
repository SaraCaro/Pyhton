import sys
import os

sys.path.append(os.path.abspath('.'))

import sqlite3
import unittest
from book import Book
from sport import Sport
from trainers import Trainers

class BookTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cls.connection.row_factory = sqlite3.Row
        cls.cur = cls.connection.cursor()
        cls.cur.execute('''CREATE TABLE book(
            id int primary key,
            date text,
            sport int
        )''')

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

    @classmethod
    def TearDownClass(cls):
        cls.cur.execute('DROP TABLE book')
        cls.connection.close()
    
    def test_constructor_AllParams_OK(self):
        # Given
        id = 1
        date = 23/5/2022
        sport = 1
        # When
        myBook = Book(BookTest.connection, id, date, sport)
        # Then
        self.assertIsNotNone(myBook)
        self.assertIsInstance(myBook, Book)
    
    # def test_load_OK(self):
    #     # Given
    #     id = 2
    #     date = '06/06/2022 18:00:00'
    #     sport_name = 'Padel'
    #     vacances = 6
    #     nombre = 'Pedro'
    #     phone = 678120445
    #     sport = Sport(self.connection,4,sport_name,vacances)
    #     trainer = Trainers(self.connection,3,nombre,phone)
    #     myBook = Book(self.connection, id, date)
    #     self.cur.execute('INSERT INTO book(id,date, sport) VALUES(?,?,?)',(id,date,sport.getID(),))
    #     self.cur.execute('INSERT INTO sports(id,name,vacances) VALUES(?,?,?)',(sport.getID(),sport_name,vacances,))
    #     self.cur.execute('INSERT INTO trainers(id,nombre,phone) VALUES(?,?,?)',(trainer.getID(),nombre,phone,))
        
    #     # When
    #     myBook.load()
    #     # Then
    #     self.cur.execute('SELECT id,date FROM book')
    #     book = self.cur.fetchone()
    #     self.assertEqual(id,book['id'])
    #     self.assertEqual(date,book['date'])
    #     self.assertEqual(sport.getID(),book['sport'])
    
    def test_Save_OK(self):
        # Given
        id = 2
        date = '06/06/2022 18:00:00'
        sport = Sport(self.connection, 8)
        myBook = Book(self.connection, id, date, sport)
        # When
        myBook._save()
        # Then
        self.cur.execute('SELECT id, date, sport FROM book WHERE id = ?', (id,))
        result = self.cur.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result['id'], id)
        self.assertEqual(result['date'], date)
        self.assertEqual(result['sport'], sport.getID())
        self.cur.execute('DELETE FROM book WHERE id = ?',(id,))

if __name__ == '__main__':
    unittest.main()
    