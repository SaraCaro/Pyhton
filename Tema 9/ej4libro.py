import math

class Fraction:
    '''Representa una fracción matematica
    que tiene su dividendo y su divisor
    '''
    def __init__ (self,dividend,divider):
        if dividend < 0:
            raise ZeroDivisionError('El dividendo no puede ser menor que 0')
        if divider <= 0:
            raise ZeroDivisionError('El divisor no puede ser 0 o menor que 0')
        # if not isinstance (dividend,int):
        #    raise TypeError('Debe proporcionar un dividendo entero')
        # if not isinstance (divider,int):
        #    raise TypeError('Debe proporcionar un divisor entero')
        self.dividend = dividend
        self.divider = divider
    
    def __str__(self):
        return f'{self.dividend}/{self.divider}'    
    
    def __add__(self,newFraction):
        if not isinstance (newFraction,Fraction):
            raise TypeError('Debe de proporcionar otra fracción')
        divider = self.divider * newFraction.divider
        numerador = (self.dividend*newFraction.dividend)+(self.divider*newFraction.divider)
        return Fraction(numerador,divider)
        
    
    def __mul__ (self,newFraction):
        if not isinstance (newFraction,Fraction):
            raise TypeError('Debe de proporcionar otra fracción')
        return Fraction (self.dividend * newFraction.dividend, self.divider * newFraction.divider)
    
    def simplify(self):
        '''Obtiene una fracción simplificada de otra
        con el mismo valor pero que ya es indivisible
        Resultado: fracción simplificada
        '''
        gcd = math.gcd(self.dividend,self.divider)
        self.dividend = int(self.dividend/gcd)
        self.divider = int(self.divider/gcd)
        return self
