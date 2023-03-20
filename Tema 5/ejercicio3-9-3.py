def maximo_valor(n1,n2,n3,n4):
    for x in range (n1,n2,n3,n4):
        valor1 = n1*n2
        valor2 = n1*n3
        valor3 = n1*n4
        valor4 = n2*n3
        valor5 = n2*n4
        valor6 = n3*n4
    print()
print ("Dime 4 números")
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

print ("El mayor producto es" + str(maximo_valor(n1,n2,n3,n4)))