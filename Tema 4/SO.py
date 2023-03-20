import os
import platform

x=os.name
if (x=="nt"):
    print ("El sistema operativo es Windows")
if(x=="posix"):
    print("El sistema operativo es Linux")
if(x=="java"):
    print("El sistema operativo es Jython")
print(platform.uname())
print("Tu directorio actual es " + str(os.getcwd()))
print ("Tus directorios y lista de archivos en la ruta actual es" + str(os.listdir()))
print("Escribe una ruta")
ruta=input()
if(os.path.exists(ruta)==True):
    print("Su lista existe" + str(os.listdir(ruta)))
if(os.path.exists(ruta)==False):
    print("La ruta no es válida")

if(os.path.isdir(ruta)==True):
    print("Su ruta es un directorio")
    print(str(os.listdir()))
elif(os.path.isfile(ruta)==True):
    print("Su ruta es un archivo")