# Ejercicio 4: comparacion de archivos

import sys
 
my_file1 = open (sys.argv[1], 'rb')
my_text1 = my_file1.read()
my_file1.close()

my_file2 = open (sys.argv[2], 'rb')
my_text2 = my_file2.read()
my_file2.close()

if my_text1 == my_text2:
    print('Los archivos son iguales')
else:
    print('Los archivos son diferentes')
