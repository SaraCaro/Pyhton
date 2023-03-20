# Programa de gestión académica, continucación

from marks_scm import (
    BadAverageError,
    MarkNotValid,
    student_data,
    show_student_list,
    average,
    filter_students_above,
    search,
    input_file,
    output_file
)

import pickle

# Valor de nota que marca el aprobado:
MARK_PASSED = 5

# Opciones del menú:
ADD_STUDENT_DATA = '1'
SHOW_STUDENT_LIST = '2'
CALCULATE_AVG = '3'
GET_NUMBER_PASSED = '4'
SHOW_STUDENTS_ABOVE_AVG = '5'
SEARCH_STUDENT = '6'
EXIT_PROGRAM = '7'

MENU_OPTIONS = (
    '1 - Añadir los datos del estudiate',
    '2 - Mostrar lista de estudiantes',
    '3 - Calcular calificación media',
    '4 - Calcular número de aprobados',
    '5 - Listar estudiantes con nota superior a la media',
    '6 - Buscar estudiantes',
    '7 - SALIR DEL PROGRAMA'
)


def show_menu():
    '''Muestra por pantalla las opciones disponibles'''
    print('\nOpciones:')
    for option in MENU_OPTIONS:
        print(option)


def process(option,student_list):
    '''Según lo que elija el usuario, se hará una de estas opciones

    option: texto que recoge el valor introducido 
    student_list: lista de diccionarios con claves para nombre y nota
    '''
    try:
        if option is ADD_STUDENT_DATA:
            choice = input("¿Ver datos de estudiantes? yes/no: ")
            if (choice == 'yes'):
                student_data(input_file, students)
                print("\nAñadiendo estudiantes...")
            elif(choice == 'no'):
                show_menu()
    except ValueError:
        print('Las notas tienen que ser con números')
        exit()
    if option is SHOW_STUDENT_LIST:
        show_student_list(student_list)
    elif option is CALCULATE_AVG:
        avg = average(student_list)
        if avg is None:
            raise BadAverageError
    elif option is GET_NUMBER_PASSED:
        students_passed = filter_students_above(student_list, MARK_PASSED)
        passed = len(students_passed)
        print('\nCantidad de aprobados: ' + str(passed))
    elif option is SHOW_STUDENTS_ABOVE_AVG:
        avg = average(student_list)
        students_above_avg = filter_students_above(student_list, avg)
        show_student_list(students_above_avg)
    elif option is SEARCH_STUDENT:
        text = input('\nIntroduce el nombre a buscar: ')
        students_matching = search(student_list, text)
        show_student_list(students_matching)




# Bloque del programa principal
try:
    input_file = input_file("students.cfg")
    output_file = output_file("students.cfg")
except IndexError:
    print("No has escrito el formato que es necesario, :")
    print("Entrada en Linea 1 = [fichero_de_entrada]")
    print("Salida en linea 4 = [fichero_de_salida]")
    exit()

try:
    with open(output_file,'rb') as stored_data:
        content = stored_data.read()
        orig_data = pickle.loads(content)
        students = orig_data
except FileNotFoundError:
    students = []
user_option = None


while user_option != EXIT_PROGRAM:
    try:
        process(user_option, students)
        show_menu()
        user_option = input('\nPor favor, seleccione una opción: ')
    except KeyboardInterrupt:
        print("\nGracias por usar este programa")
        exit()

if user_option == EXIT_PROGRAM:
    with open(output_file,'wb') as students_file:
        students_data = pickle.dumps(students)
        students_file.write(students_data)