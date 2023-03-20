# Ejercicio 8:

from sys import argv

def show_syntax():
    print ('Sintaxis: ejercicio8 <numero1> <numero2>')
    print ('Sintaxis: valor entre 1 y 10')
    print ('Sintaxis: valor entre 0 y 10')
    exit()
    
def validated_param(number_as_text,low_limit,upper_limit):
    try:
        number = int(number_as_text)
        print('Numero introducido: ', number)
    except ValueError:
        show_syntax()
    if number < low_limit or number > upper_limit:
        show_syntax()
        return number
        
# Validación del los números introducidos
number = None
if len (argv) < 3:
    show_syntax()
number1 = validated_param(argv[1],1,10)
number2 = validated_param(argv[2],0,10)
    
# 
filename = f'tabla-{number}.txt'

with open(filename, 'rt') as my_file:
    content = my_file.readlines()
    print(content[number2])
