i=0
par=0
impar=0
positivo=0
negativo=0

print ("Dame un número")
x=float(input())
while (x!=0):
    if (x%2==0):
        par=par+1
    elif (x%2!=0):
        impar=impar+1
    if (x>0):
        positivo=positivo+x
    elif (x<0):
        negativo=negativo+x
    print("Dame otro número")
    x=float(input())
    i=i+1
media=(negativo+positivo/2)

print(" ")
print("Se han introducido " + str(i) + " numeros en total")
print("Hay " + str(par) + " números pares y " + str(impar) + " numeros impares")
print("Hay en total " + str(positivo) + " números positivos y " + str(negativo) + " números negativos")
print("La media de los números introducidos es " + str(media))