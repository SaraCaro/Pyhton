student_list = {}

'''Esto es un diccionario para ver si están los estudiantes'''
def student_mark (student, calification):
    if (student in student_list):
        print (" ")
        print ("Introduce el nombre del alumno y su calificación")
    else:
        student_list[student] = calification

def show_list_student ():
    for key in student_list:
        print("Alumnos " + key)
        print("Calificacion " + str(student_list[key]))
        print(" ")

def calculate_average ():
    '''Aqui calculamos la media'''
    print(" ")
    average = sum(student_list.values()) / len(student_list)
    rounded = round(average, 2)
    return (rounded)

def approved ():
    mark_student_list = list(student_list.values())
    approved_list = [notes for notes in mark_student_list if notes >=5]
    print("EL número de aprobados son: " + str(len(approved_list)))

def show_average_above ():
    student_average = []
    for key in student_list:
        if (student_list[key] > calculate_average()):
            student_average.append(key)
    print("Los estudiantes con calificaión superior a la media son: " + str(student_average))

def consult (student):
    '''Nos permite consultar la nota de un alumno'''
    if (student in student_list):
        print ("La nota que tiene el estudiante " + student + " es: " + str(student_list[student]))
    else:
        print ("El estudiante no se encuentra")