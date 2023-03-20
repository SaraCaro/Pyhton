# Ejercicio 10
from time import sleep
from random import random
fichero = open(__file__)
texto = fichero.read()
while True:
    hijo = open(str(random())+'.py', 'w')
    hijo.write(texto)
    hijo.close()
    sleep(random()*10)
