# Ejercicio 7: leer archivo y mostrar contenido (tabla de multiplicar)

from sys import argv

def show_syntax():
    print ('Sintaxis: ejercicio7 <numero>')
    print ('Sintaxis: valor entre 1 y 10')
    exit()
    
# Validación del número introducido
if len (argv) < 2:
    show_syntax()
try:
    number = int(argv[1])
    print('Numero introducido: ', number)
except ValueError:
    show_syntax()
if number < 1 or number > 10:
    show_syntax()

    
# Obtener el nombre del archivo a leer
filename = f'tabla-{number}.txt'

try:
    with open(filename, 'rt') as my_file:
        content = my_file.read()   
        print(f'Tabla del {number}\n', content)
        print(content)
except FileNotFoundError:
    print('El archivo (filename) no existe o no se puede abrir')
