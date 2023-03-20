# Ejercicio 3: sustituir una palabra en un archivo

import sys

with open (sys.argv[1], 'r+') as my_file:
    my_text = my_file.read()
    result = my_text.replace(sys.argv[2], sys.argv[3])
    my_file.seek(0) #posicionamos el puntero al principio para borrar
    my_file.truncate()
    my_file.write(result)

    
    
