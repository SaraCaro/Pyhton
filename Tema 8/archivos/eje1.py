import sys

my_file = open(sys.argv[1], 'a')
while True:
    try:
        line = input('Introduzca texto: ')
        my_file.write('\n' + line)
    except KeyboardInterrupt:
        break
print('Fin del programa')
my_file.close()
