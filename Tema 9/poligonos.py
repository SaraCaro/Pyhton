import math

class RegularPolygon:
    def __init__(self,length,sideNum):
        if sideNum < 3:
            raise ValueError('Debe proporcionar como mínimo un valor de 3')
        if length <= 0:
            raise ValueError('Debe proporcionar un valor mayor que 0')
        self.length = length
        self.sideNum = sideNum

    def perimeter(self):
        perimeter = self.length * self.sideNum
        return perimeter

    def apotema(self):
        apotema = self.length / (2 * math.tan(math.pi / self.sideNum))
        return apotema

    def area(self):
        area = (self.perimeter * self.apotema) / 2
        return area

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
