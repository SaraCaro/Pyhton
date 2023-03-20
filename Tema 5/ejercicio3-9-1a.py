def calcular (horas,minutos,segundos):
    segundos_totales=3600 * horas + 60 * minutos + segundos
    print("Son", segundos_totales, "segundos")
print("Introduce horas, minutos y segundos")
horas=int(input())
minutos=int(input())
segundos=int(input())
print (calcular(horas,minutos,segundos))