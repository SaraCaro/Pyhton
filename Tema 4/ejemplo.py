i=0
import time

inicio=time.time()
print("Dime tu nombre")
nombre= input()
fin=time.time()
x=int(fin-inicio)
i=int(x/60)
s=x%60
print ("Han pasado " + str(i) + "minutos y " + str(s) + "segundos")
