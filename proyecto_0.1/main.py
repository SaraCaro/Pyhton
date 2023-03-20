import sqlite3

from sportManager import SportManager
from trainersManager import TrainerManager
from sport import Sport
from book import Book
from datetime import datetime
from exceptions import OldDateException
from exceptions import FullClassInThisSport
from exceptions import BusyTime


def show_menu():
    opt = False
    user_opt = -1
    while not opt:
        print('1. Listar todos los deportes ofertados')
        print('2. Listar todos los entrenadores ofertados')
        print('3. Deporte con mayor numero de vacantes')
        print('4. Reservar entreno') # que no haya plazas + que ya haya una reserva ese dia
        user_opt = int(input('Introduce opcion: '))
        if not (user_opt < 1 or user_opt >3): opt = True
    return user_opt

try:
    opt = show_menu()
    db =  sqlite3.connect('pabellon.db')


    if opt == 1:
        sport = SportManager(db)
        for i in sport.get_all_saved_sports(): # SportManager
            print(i)
    elif opt == 2:
        trainers = TrainerManager(db)
        for i in trainers.get_all_saved_trainers(): # TrainersManager
            print(i)
    elif opt == 3:
        sport = SportManager(db)
        for i in sport.get_max_vacances(): # SportManager
            print(i)
    elif opt == 4:
        correct_date = False
        while not correct_date:
            date = input('Introduce una fecha: ')
            correct_date = Book.check_hours_format(date)
        try:
            date = datetime.strptime(date, '%d/%m/%Y %H:%M')
        except ValueError:
            print('El formato de la fecha es inválido')


        sport = int(input('Introduce el deporte que quieres reservar: '))
        s = Sport(db, sport)
        s.load()
        try:
            Book(db, None, date, s).save()
        except OldDateException as e1:
            print(e1)
        except FullClassInThisSport as e2:
            print(e2)
        except BusyTime as e3:
            print(e3)
except KeyboardInterrupt:
    print('\n\nPrograma interrumpido por el usuario')