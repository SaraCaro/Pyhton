import mark_scm

print("1. Añadir estudiante y calificación")
print("2. Mostrar lista de estudiantes con sus calificaciones")
print("3. Calcular la media de las calificaciones de toda la clase")
print("4. Calcular el número de aprobados")
print("5. Mostrar los estudiantes con calificación superior a la media")
print("6. Consultar la nota de un estudiante determinado")
print("7. Finalizar programa")
print("Seleccione una opción")
print(" ")

user = int(input())

while (user != 7 ):
    if (user > 7 or user < 1): 
        print(" ")
        print ("Introduce un número que sea válido")  

    if (user == 1):
        print (" ")
        print ("Introduce el nombre del estudiante y su calificación")
        mark_scm.student_mark(input("Estudiante "), float(input("Calificación ")))

    if (user == 2):
        print("")
        print("Lista de estudiantes y sus calificaciones")
        mark_scm.show_list_student()
    
    if (user== 3):
        print(" ")
        print("La media de las calificaciones es: " + str(mark_scm.calculate_average))
    
    if (user == 4):
        mark_scm.approved()
    
    if (user == 5):
        mark_scm.show_average_above()

    if (user == 6):
        print(" ")
        print("Escribe el nombre del estudiante del que quieras saber la nota: ")
        mark_scm.consult(input("Estudiante: "))

    print("1. Añadir estudiante y calificación")
    print("2. Mostrar lista de estudiantes con sus calificaciones")
    print("3. Calcular la media de las calificaciones de toda la clase")
    print("4. Calcular el número de aprobados")
    print("5. Mostrar los estudiantes con calificación superior a la media")
    print("6. Consultar la nota de un estudiante determinado")
    print("7. Finalizar programa")
    print("Seleccione una opción")
    print(" ")
    
    user = int(input())
#Este if me permite salir del while
if (user == 7):
        quit()