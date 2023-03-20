# Ejercicio 2: linea mas corta / larga

import sys

shortest_line = None
longest_line = ''
with open(sys.argv[1]) as my_file:
    for line in my_file:
        if len(line) > len(longest_line):
            longest_line = line
        if shortest_line is None or len(line) < len(shortest_line):
            shortest_line = line
print('Resultado: ')
print('Línea mas corta: ', shortest_line)
print('Línea mas larga: ', longest_line)
        
        
