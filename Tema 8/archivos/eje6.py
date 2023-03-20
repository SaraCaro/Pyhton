# Ejercicio 6

from sys import argv

def show_syntax():
    print ('Sintaxis: ejercicio6 <numero>')
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

# Creaccion de archivo
# filename = 'tabla-' + str(number) + .txt
filename = f'tabla-{number}.txt'
my_file = open(filename,'wt')
for i in range(0,11):
    result = i * number
    line = f'{number}· {i} = {result}\n'
    my_file.write(line)
my_file.close()
