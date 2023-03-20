def calcular (horas,minutos,segundos):
    segundos_totales=3600 * horas + 60 * minutos + segundos
    print("Son", segundos_totales, "segundos")
print("Introduce horas, minutos y segundos")
horas=int(input())
minutos=int(input())
segundos=int(input())
print (calcular(horas,minutos,segundos))
def conversor (segundos):
    total_horas=int(segundos/3600)
    total_minutos=int(segundos-total_horas*3600/60)
    total_segundos=int(segundos-total_horas-total_minutos*3600/60)
    print("En total hay " + str(total_horas) + " horas, " + str(total_minutos)+ "minutos, " + str(total_segundos) +"segundos")
print ("Introduce segundos")
segundos=int(input())
print(conversor(segundos))
