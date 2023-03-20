def find_archive(file):
    try:
        with open(file, 'rb') as content_file:
            content = content_file.read()
            return content
    except FileNotFoundError:
        print("No existe el archivo")

def store_data (name,mark,phone_number,email,student_list):
    '''Añade nuevos datos a la lista de estudiantes incluyendo su nombre
    y su nota.

    name: cadena de texto para añadir nombre 
    mark: número que indica la nota del estudiante 
    phone_number: número de telefono del estudiante
    email: cadena de texto con el correo electrónico del estudiante
    student_list: lista con el nombre y nota del estudiante (list)
    '''
    if mark < 0 or mark > 10:
            raise MarkNotValid(mark)
    student = {}
    student['name'] = name
    student['mark'] = mark
    student['phone_number'] = phone_number
    student['email'] = email
    student_list.append(student)

def student_data(file, student_list):
    '''Carga en memoria el contenido del fichero indicado, añadiendo su contenido
    a la lista de estudiantes si este contiene el formato correcto.

    student_list: lista de registros con nombre y nota (list)
    file: fichero donde está la lista de estudiantes
    '''
    with open(file) as student_file:
        for line in student_file:
            no_spaces = " ".join(line.split())
            store_students_list = no_spaces.split(",")
            try:
                name = store_students_list[0]
                mark = float(store_students_list[1])
                phone_number = store_students_list[2]
                email = store_students_list[3]
            except IndexError:
                print("\nNo dejar lineas en blanco\n")
                exit()
            student_data(name, mark, phone_number, email, student_list)

def show_student_list(student_list):
    '''Muestra por pantalla el nombre y la nota de cada estudiante de la lista.

    student_list: lista de diccionarios donde cada elemento tiene índices
                  ('name', 'mark', 'phone_number' y 'email')
                   para representar los datos de cada alumno.
    '''
    print('\nLista de estudiantes:')
    for student in student_list:
        print('\nNombre : ' + student['name'])
        print('Calificación : ' + str(student['mark']))
        print('Número de teléfono : ' + student['phone_number'])
        print('Correo electrónico : ' + student['email'])


def average(student_list):
    '''
    Calcula el valor de la media aritmética de las notas incluidas
    en la lista de estudiantes.

    student_list: lista de diccionarios donde cada elemento tiene índices
                  ('name' y 'mark') para representar los datos de cada alumno.

    Resultado: valor de la media (float).
               Si la lista no tiene elementos devuelve None.
    '''
    if len(student_list) == 0:
        return None
    total_sum = 0
    for student in student_list:
        total_sum += student['mark']
    return total_sum / len(student_list)


def filter_students_above(student_list, threshold):
    '''Obtiene una relación de aquellos estudiantes de la lista
    cuya calificación está por encima del límite indicado.

    student_list: lista de diccionarios donde cada elemento tiene índices
                  ('name' y 'mark') para representar los datos de cada alumno.
    threshold: umbral de la nota (float)

    Resultado: lista de diccionarios con nombre y nota (índices 'name', 'mark')
    '''
    result = []
    for student in student_list:
        if student['mark'] >= threshold:
            result.append(student)
    return result


def search(student_list, text):
    '''Localiza aquellos estudiantes cuyo nombre contiene el texto indicado.
    No se hace distinción entre mayúsculas y minúsculas.

    student_list: lista de diccionarios donde cada elemento tiene índices
                  ('name', 'mark', 'phone_number', 'email') para representar los datos de cada alumno.
    text: parte del nombre que debe contener cada registro del resultado (str).

    Resultado: lista de diccionarios con nombre y nota (índices 'name', 'mark')
    '''
    result = []
    text = text.lower()
    for student in student_list:
        if text in student['name'].lower():
            result.append(student)
        else:
            raise NoStudentError(text)
    return result

def input_file(file):
    '''Busca el fichero de entrada si el fichero
    cumple con el formato correcto:

    file: fichero a abrir.

    Resultado: es una cadena de texto con fichero de entrada.
    '''
    try:
        with open(file) as configuration_file:
            input_no_spaces = "".join(configuration_file.readline().split())
            input_list = input_no_spaces.split("=")
            input_file = input_list[1]
            return input_file
    except FileNotFoundError:
        print("\nNo existe el archivo\n")
        exit()

def output_file(file):
    '''Busca el fichero de salida si el fichero
    cumple con el formato correcto:

    file: fichero a abrir.

    Resultado: es una cadena de texto con fichero de entrada.
    '''
    with open(file) as configuration_file:
        output_line = configuration_file.readlines()[3]
        output_no_spaces = "".join(output_line.split())
        output_list = output_no_spaces.split("=")
        output_file = output_list[1]
        return output_file

class NoStudentError(Exception):
    """Muestra que no se encuentra al estudiante buscado

    Atributos:  student--> nombre del estudiante que se busca
                message-->   texto informativo 
    """

    def __init__(self, student, message = "Error: El estudiante no está en la lista "):
        self.student = student
        self.message = message + str(student)
        super().__init__(self.message)

class MarkNotValid(Exception):
    """Muestra que la nota no es válida

    Atributos:  mark--> nota introducida
                message-->   texto informativo  
    """

    def __init__(self, mark, message = "Error: Nota no válida. Tiene que ser mayor que 0 y menor que 10 "):
        self.mark = mark
        self.message = message + mark
        super().__init__(self.message)

class BadAverageError(Exception):
    """Muestra que no hay valores
    Atributos:  message-->   texto informativo 
    """

    def __init__(self, message = "Error: La media no fue calculada correctamente. "):
        self.message = message
        super().__init__(self.message)
