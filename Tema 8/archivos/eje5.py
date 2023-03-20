# Ejercicio 5: copiar un archivo

import sys

my_file = open(sys.argv[1], 'rb')
data = my_file.read()
my_file.close()

my_file_copy = open(sys.argv[2], 'wb')
my_file_copy.write(data)
my_file_copy.close()
