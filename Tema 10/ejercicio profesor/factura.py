from articulo import Article


class Bill:
    '''Representa facturas'''
    def __init__(self,numero,cliente,lineas):
        self.numero = numero
        self.cliente = cliente
        self.lineas = lineas
    
    def __str__(self):
        return f'Factura {self.numero} del cliente {self.cliente}'

