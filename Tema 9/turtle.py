import math
import turtle

class RegularPolygon:

    color = 'white'

    def __init__(self,length,sideNum):
        if sideNum < 3:
            raise ValueError('Debe proporcionar como mínimo un valor de 3')
        if length <= 0:
            raise ValueError('Debe proporcionar un valor mayor que 0')
        self.length = length
        self.sideNum = sideNum
        self.my_color = None


    def __eq__(self,polygon):
        return self.length == polygon.length and self.sideNum == polygon.sideNum

    def __ge__(self,polygon):
        return self.sideNum >= polygon.sideNum and self.length >= polygon.length

    def __gt__(self,polygon):
        return self.length > polygon.length and self.sideNum > polygon.sideNum

    def __le__(self,polygon):
        return self.sideNum <= polygon.sideNum and self.length <= polygon.length

    def __lt__(self,polygon):
        return self.length < polygon.length and self.sideNum < polygon.sideNum

    def __str__(self):
        return f'{self.length}{self.sideNum}'


    @classmethod
    def setDefaultColor(cls,color):
        '''Establecemos un color por defecto para todos los polígonos
        color: color expresado en inglés(str)
        '''
        cls.color = color 

    def perimeter(self):
            perimeter = self.length * self.sideNum
            return perimeter

    def apotema(self):
            apotema = self.length / (2 * math.tan(math.pi / self.sideNum))
            return apotema

    def area(self):
            area = (self.perimeter * self.apotema) / 2
            return area
    

    def setColor(self,color):
        '''Establecemos un color por defecto para este polígono
        color: color expresado en inglés(str)
        '''
        self.my_color = color
    
    def draw(self):
        '''Pinta el poligono y relleno del color correspondiente
        (si objeto tiene color, se pinta del mismo, sino, se pinta
        del color por defecto)
        '''
        # if hasattr(self, 'my_color'):
        if self.my_color != None:
            color = self.my_color
        else:
            color = RegularPolygon.color
        print(color)
        turtle.fillcolor(color)
        turtle.begin_fill()
        for i in range(self.sideNum):
            turtle.forward(self.length)
            turtle.right(360/self.sideNum)
        turtle.end_fill()
        #turtle.done()
