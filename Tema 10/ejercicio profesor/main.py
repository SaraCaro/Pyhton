from cliente import Client
from articulo import Article
from factura import Bill

pedro = Client(7729934, 'Pedro','Espigares',)
print(pedro)

articulo = Article(345,'Teclado',10.8)
print(articulo)

factura = Bill(23,'Pedro',articulo)
print(factura)