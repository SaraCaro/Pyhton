# b
import sys

matriz= [
    [2, 0, 3, -1],
    [3, -2, 10, 9],
    [5, 1, 7, 7],
]

with open (sys.argv[1], 'wt') as my_file:
    num_filas = len(matriz)
    num_columns = len(matriz[0])
    first_line = str(num_filas) + ' '+ str(num_columns)+'\n'
    # f'{num_filas} {num_columns}\n'
    my_file.write(first_line)
    for row in matriz:
         line = ''
         for element in row:
             line += str(element)+ ' '
         line = line.rstrip()+'\n'
         my_file.write(line)
    
    
    
    



