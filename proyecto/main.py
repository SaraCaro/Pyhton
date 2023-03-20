
from sport import Sport
from trainers import Trainers
from db_manager import DBManager
from book import Book

from datetime import datetime

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

def check_hours_format(time):
    t = time.split(' ') # [12/12/2012, 10:45]
    return t[1] in ['16:00', '17:00', '18:00', '19:00', '20:00']

opt = show_menu()

db = DBManager() 
if opt == 1:
    sport = Sport(db)
    for i in sport.load(): # SportManager
        print(i)
elif opt == 2:
    trainers = Trainers(db)
    for i in trainers.load(): # Trainers manager
        print(i)
elif opt == 3:
    trainer = 1#int(input('ID del entrenador: '))
    sport = 1#int(input('ID del deporte: '))
    hora = '6/5/22 16:00' #input('Introduce hora y dia de la reserva: d/m/y h:m: ')
    if check_hours_format(hora):
        date_time_obj = datetime.strptime(hora, '%d/%m/%y %H:%M')
        print(date_time_obj)
        b = Book(db).insert(date_time_obj, sport, trainer)
        print(b)
elif opt == 4:
    print('Elimina 2 y 3 auto')
    Book(db).delete('2')
    Book(db).delete('3')


