import math

class Points:
    '''Representa un punto en 2D con coordenadas
    X e Y'''

    def __init__(self,y = 0,x = 0):
        if not isinstance (y, int) or not isinstance (x,int):
            raise ValueError('Los valores deben ser numericos')
        else:
            self.y = y
            self.x = x
        
    def __str__(self):
        return f'{self.x},{self.y}'
    
    def quadrant(self):
        '''Determina en qué cuadrante se encuentra el punto'''
        if self.x > 0 and self.y > 0:
            print('El punto está situado en el cuadrante superior derecho (1)')
        elif self.x < 0 and self.y > 0:
            print('El punto está situado en el cuadrante superior izquierdo (2)')
        elif self.x > 0 and self.y < 0:
            print('El punto está situado en el cuadrante inferior derecho (3)')
        elif self.x < 0 and self.y < 0:
            print('El punto está situado en el cuadrante inferior izquierdo (4)')
        elif self.x == 0 and self.y == 0:
            print('El punto está situado en el origen de coordenadas')

    def calculateDistance(self,anotherPoint):
        '''Calcula el valor de la distancia entre dos puntos
        anotherPoint: objeto de la clase (Points) 
        resultado: valor numerico(float)
        '''
        distance = math.sqrt((anotherPoint.x - self.x)**2
        + (anotherPoint.y - self.y)**2)
        return distance

punto = Points(3,7)
punto2 = Points(1,10)
print(punto2)
print(punto2.calculateDistance(punto))