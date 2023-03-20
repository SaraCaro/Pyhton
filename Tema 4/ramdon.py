import random

r=random.randrange (0,10)
print("Adivina el número")
x=int(input())
while (x!=r):
    if (x>r):
        print("El número es menor, introduce otro número")
        x=int(input())
    elif (x<r):
        print("El número es mayor, introduce otro número ")
        x=int(input())
print("¡Has acertado!")
