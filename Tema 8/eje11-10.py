import sys

def head():
  try:
    nombre = str(input('Dime el nombre del archivo a procesar: '))
    N = int(input('Dime el numero de lineas a imprimir: '))
    with open(nombre+'.txt') as ar:
      for i in range(N):
        print( ' - ' + ar.readline())
    ar.close()
  except ValueError as V:
    print('\n error: debe ser un numero entero ')
  except FileNotFoundError as E: 
    print('el archivo con el nombre especificado no se encuentra')

head()

def head(filename, num_lines):
    my_file = open(filename)
    for i in range(num_lines):
        line = my_file.readline()
        print(line)
    my_file.close()

head(sys.argv[1], int(sys.argv[2]))