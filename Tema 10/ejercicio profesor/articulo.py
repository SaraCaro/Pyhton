class Article:
    '''Representa articulos'''
    def __init__(self,codigo,denominacion,precio):
        self.codigo = codigo
        self.denominacion = denominacion
        self.precio = precio
    
    def __str__(self):
        return f'El codigo es: {self.codigo}, Denominacion: {self.denominacion} y precio: {self.precio}'

    def calcularTotal(self):
        total = 0.0

