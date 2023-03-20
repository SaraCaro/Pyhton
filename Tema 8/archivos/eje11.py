# Ejercicio 11: 

import sys

with open(sys.argv[1]) as origin_file:
    content = origin.file.read()
    upper_content = content.upper()

with open(sys.argv[2]) as dest_file:
    dest_file.write(upper.content)
