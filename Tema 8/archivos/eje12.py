# Ejercicio 12: ejercicio matrices

# a
import sys

def convert_number(my_list):
    ''' Convertir los elementos de la lista en número

    my_list: es una lista de cadenas de texto con
    caracteres numéricos
    resultado: Lista de números enteros
    '''
    result = []
    for element in my_list:
        result.append(int(element))
    return(result)
    
with open (sys.argv[1]) as matrix_file:
    first_line = matrix_file.readline()
    lista = first_line.split()
    num_filas = int(lista[0])
    # num_columns = [1]
    matrix = []
    for i in range(1,num_filas+1):
        current_line = matrix_file.readline()
        values = current_line.split()
        result_convert = convert_number(values)
        matrix.append(result_convert)
    print(matrix)




        
        
        
