from marks_scm import (
    BadAverageError,
    student_data,
    show_student_list,
    average,
    filter_students_above,
    search,
    input_file,
    output_file
)

import sys

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


def write_students(file,student_list):
    '''Escribe en un archivo binario la lista de estudiantes que
    hay en la memoria

    file: fichero donde se va a escribir la lista
    student_list: lista de diccionarios con claves para nombre, nota, teléfono
    y correo electrónico
    '''
    with open(file,"wb") as students_file:
        students_data = pickle.dumps(student_list)
        students_file.write(students_data)


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
                write_students(output_file,student_list)
            elif(choice == "no"):
                exit()
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
        text = sys.argv[2]
        students_matching = search(student_list, text)
        show_student_list(students_matching)


# Bloque del programa principal
try:
    input_file = input_file("students.cfg")
    output_file = output_file("students.cfg")
except FileNotFoundError:
    print("\nNo existe el archivo\n")

try:
    with open(output_file,'rb') as stored_data:
        content = stored_data.read()
        orig_data = pickle.loads(content)
        students = orig_data
except FileNotFoundError:
    students = []
user_option = sys.argv[2]
    
try:
    process(user_option, students)
except KeyboardInterrupt:
    print("\nGracias por usar este programa")
    exit()
    

