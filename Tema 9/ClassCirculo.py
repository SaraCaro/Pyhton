from ClassFigura import Figure
import math
import turtle


class Circle(Figure):
    '''Representa círculos con un radio proporcionado
    por parámetro y algunas de sus operaciones más
    habituales.
    
    Hereda de la clase Figure'''
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Debe proporcionar un valor superior a 0")
        self.radius = radius
        super().__init__()

    
    def __eq__(self,anotherCircle):
        if not isinstance(anotherCircle,Circle):
            return False
        else:
            return self.radius == anotherCircle.radius

    
    def __str__(self):
        return f'Círculo de {self.radius} de radio'

    
    def calculatePerimeter(self):
        '''Calcula el perímetro del circulo
        según su radio
        
        radius: radio del circulo

        resultado: perímetro
        '''
        perimeter = 2 * math.pi * self.radius
        return perimeter

    
    def calculateArea(self):
        '''Calcula el área del círculo según
        su radio

        radius: radio del circulo

        resultado: area
        '''
        area = math.pi * (self.radius**2)
        return round(area,2)
    

    def draw(self):
        '''Pinta el circulo relleno del color correspondiente
        (Si el objeto tiene color, se pinta del mismo, si no, 
        se pinta del color por defecto).
        '''
        if self.mycolor != None:
                color = self.mycolor
        else:
            color = self.color
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(self.radius)
        turtle.end_fill()
        #turtle.done()

