import sqlite3

from contact_scm import Contact
from quote_scm import Quotes
from schedule_scm import ScheduleManager

conn = sqlite3.connect('./agenda_scm.db')

def probarManager():
    manager = ScheduleManager(conn)
    contactsSet = manager.loadByFile('archive.txt')
    for contacto in contactsSet:
        contacto.save()

def pruebaManagerGetByIds():
    manager = ScheduleManager(conn)
    rtado = manager.getByIdsContact(1, 2, 3)
    for i in rtado:
        print(i)

def pruebaManagerGetBySth():
    manager = ScheduleManager(conn)
    
    # rtado = manager.getByTelephoneContact(63)
    # for i in rtado:
    #     print(i)

    # rtado = manager.getByAddressContact('jar')
    # for i in rtado:
    #     print(i)
    # rtado = manager.getByEmailContact('micorreo')
    # for i in rtado:
    #     print(i)

    rtado = manager.getByDateQuote('/')
    for i in rtado:
        print(i)
    # rtado = manager.getByContactsQuote(contacto2)
    # for i in rtado:
    #     print(i)


# main -------------------------
pruebaManagerGetByIds()  
# pruebaManagerGetBySth()  


contacto1 = Contact(conn,1,'Pedro','Espigares Asenjo','pedro@gmail.com',678536923,'C/Fernando de los Rios')
# contacto1.save()

contacto2 = Contact(conn,2,'Luis','Moya Prados',None,602849201,'Gójar')
# contacto2.save()
agenda1 = ScheduleManager(conn)
agenda1.getByContactsQuote(contacto2)

contacto3 = Contact(conn,3,'Sofia','Benavides Fernandez','sofia@gmail.com',639270326,'Zaidin')
# contacto3.save()

# contacto4 = Contact(conn,4,'Clara','Garcia Iop','clara@gmail.com',629045734,'Realejo')
# contacto4.save()
# contacto4.delete()
# contacto4.load()

# citas = Quotes(conn,1,contacto1,'Hacer Trabajo','Biblioteca',None,None)
# citas.save()
# citas.delete()

# cita2 = Quotes(conn,2,contacto2,'Tomar unas tapas','Bar RhinBarril','29/4/2022',None)
# cita2.save()

# cita3 = Quotes(conn,3,contacto3,'Ir a bailar','Escuela BasMove',None,'20:00')
# cita3.save()
# cita3.delete()

# cita4 = Quotes(conn,4,contacto4,'Ver pelicula','Cine Neptuno','3/5/2022','19:00')
# cita4.save()

# hasID = Quotes(conn,1,[contacto1,contacto2,contacto3],'Comprar Pan','Panaderia')
# hasID.saveQuote_Contacts()