# Ejercicio 11.10.4

import sys

with open(sys.argv[1]) as my_file:
    for line in my_file:
        if sys.argv[2] in line:
            print(line)
            
        
        

