def conversor (segundos):
    total_horas=int(segundos/3600)
    total_minutos=int(segundos-total_horas*3600/60)
    total_segundos=int(segundos-total_horas-total_minutos*3600/60)
    print("En total hay " + str(total_horas) + " horas, " + str(total_minutos)+ "minutos, " + str(total_segundos) +"segundos")
print ("Introduce segundos")
segundos=int(input())
print(conversor(segundos))
