import sqlite3

from sportManager import SportManager
from trainersManager import TrainerManager
from sport import Sport
from book import Book
from datetime import datetime
from exceptions import OldDateException

def show_menu():
    opt = False
    user_opt = -1
    while not opt:
        print('1. Listar todos los deportes ofertados')
        print('2. Listar todos los entrenadores ofertados')
        print('3. Reservar entreno') # que no haya plazas + que ya haya una reserva ese dia
        print('4. Obtener mi gasto del mes')
        print('5. Obtener el deporte mas solicitado')
        user_opt = int(input('Introduce opcion: '))
        if not (user_opt < 1 or user_opt >5): opt = True
    return user_opt


opt = 1
db =  sqlite3.connect('pabellon.db')


if opt == 1:
    sport = SportManager(db)
    for i in sport.get_all_saved_sports(): # SportManager
        print(i)
elif opt == 2:
    trainers = TrainerManager(db)
    for i in trainers.get_all_saved_trainers(): # Trainers manager
        print(i)
elif opt == 3:
    correct_date = False
    while not correct_date:
        date = '16/06/2022 17:00'#input('Introduce una fecha: ')
        correct_date = Book.check_hours_format(date)
    try:
        date = datetime.strptime(date, '%d/%m/%Y %H:%M')
    except ValueError:
        print('Formato de la fecha es inválido')


    sport = 2#int(input('Introduce el deporte que quieres reservar: '))
    s = Sport(db, sport)
    s.load()
    try:
        Book(db, None, date, s).save()
    except OldDateException as e1:
        print(e1)
