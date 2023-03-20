from shutil import register_unpack_format
from ClassFigura import Figure
import math
import turtle


class RegularPolygon(Figure):
    '''Representa polígonos regulares de un número de lados
    y una longitud de lados proporcionada por parámetros y
    algunas de sus operaciones más habituales

    Hereda de la clase Figure'''
    def __init__(self, sideLenght, sideNum):
        if sideNum < 3:
            raise ValueError("Debe proporcionar como mínimo un valor de 3")
        if sideLenght <= 0:
            raise ValueError("Debe proporcionar un valor superior a 0")
        self.sideLenght = sideLenght
        self.sideNum = sideNum
        super().__init__()


    def __eq__(self, anotherPolygon):
        if not isinstance(anotherPolygon,RegularPolygon):
            return False
        else:
            return self.sideNum == anotherPolygon.sideNum and self.sideLenght == anotherPolygon.sideLenght
    
    
    def __str__(self):
        return f'Polígono con {self.sideNum} lados y {self.sideLenght} de longitud cada lado'
    

    def calculatePerimeter(self):
        '''Calcula el perímetro del polígono según su número de lados
        y la longitud de cada lado
        
        sideLenght: longitud del lado
        sideNum: número de lados

        resultado: perímetro
        '''
        perimeter = self.sideLenght * self.sideNum
        return perimeter


    def calculateApothem(self):
        '''Calcula la apotema del polígono según su número de lados
        
        sideNum: número de lados

        resultado: apotema
        '''
        apothem = self.sideLenght / (2* math.tan(math.pi/self.sideNum))
        return apothem


    def calculateArea(self):
        '''Calcula el área del polígono según su perímetro
        y su apotema
        
        calculatePerimeter: perímetro del polígono
        calculateApothem: apotema del perímetro

        resultado: area
        '''
        area = (self.calculatePerimeter() * self.calculateApothem()) / 2
        return round(area,2)
        

    def draw(self):
            '''Pinta el polígono relleno del color correspondiente
            (Si el objeto tiene color, se pinta del mismo, si no, 
            se pinta del color por defecto).
            '''
            #if hasattr(self,"mycolor")
            if self.mycolor != None:
                color = self.mycolor
            else:
                color = RegularPolygon.color
            turtle.fillcolor(color)
            turtle.begin_fill()
            for i in range(self.sideNum):
                turtle.forward(self.sideLenght)
                turtle.right(360/self.sideNum)
            turtle.end_fill()
            #turtle.done()

