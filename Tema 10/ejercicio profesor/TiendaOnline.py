class Customer:
    '''Define un cliente con dni, nombre y apellidos'''

    def __init__(self ,dni, name, surname):
        self.dni = dni
        self.name = name
        self.surname = surname


class Article:
    '''Define un artículo con código, denominación y precio'''

    def __init__(self, id, denomination, price):
        self.id = id
        self.denomination = denomination
        self.price = price


class Invoice:
    '''Define una factura con numero, cliente y líneas'''

    def __init__(self, number, customer, rows):
        self.number = number
        self.customer = customer
        self.rows = rows


    def TotalPrice(self):
        total = 0
        for row in self.rows:
            total += row.subtotal
        return total


class InvoiceLine:
    '''Define una línea de factura con un artículo y la cantidad'''

    def __init__(self, article, amount, subtotal = 0):
        self.article = article
        self.amount = amount
        self.subtotal = self.Subtotal()

    def Subtotal(self):
        subtotal = self.article.price * self.amount
        return subtotal

persona = Customer(22342, "Pepe", "Juan")

art1 = Article(3,"España", 5.5)
linea1 = InvoiceLine(art1, 2)
print("Precio línea 1: ", linea1.Subtotal(), "€")

art2 = Article(5,"Portugal", 7)
linea2 = InvoiceLine(art2, 4)
print("Precio línea 2: ", linea2.Subtotal(), "€")

lineas = (linea1, linea2)
factura = Invoice(1, persona, lineas)
print("Precio total de la factura: ", factura.TotalPrice(), "€")