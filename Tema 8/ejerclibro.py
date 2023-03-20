# Ejercicio 11.10.3 libro

import sys

n_lines = 0
n_words = 0
n_chars = 0
with open(sys.argv[1]) as my_file:
    for line in my_file:
        n_lines += 1
        n_chars += len(line)
        n_words += len(line.split())
        
print('El número de lineas que hay en el archivo es: ' + str(n_lines))
print('El número de palabras que hay en el archivo es:',n_words)
print(f'El número de caracteres que hay en el archivo es: {n_chars}')
