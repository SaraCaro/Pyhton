class Figure:

    color = "white"


    def __init__(self):
        self.mycolor = None
        
        
    def __ge__(self, anotherFigure):
        return self.calculateArea() >= anotherFigure.calculateArea()
    

    def __gt__(self, anotherFigure):
        return self.calculateArea() > anotherFigure.calculateArea()
    

    def __le__(self, anotherFigure):
        return self.calculateArea() <=  anotherFigure.calculateArea()
        

    def __lt__(self, anotherFigure):
        return self.calculateArea() < anotherFigure.calculateArea()


    @classmethod
    def setDefaultColor(cls, color):
        '''Establece un color por defecto para todos los polígonos
        
        color: color expresado en inglés (str)
        '''
        cls.color = color


    def setColor(self, color):
        '''Establece un color por defecto para este polígono
        
        color: color expresado en inglés (str)
        '''
        self.mycolor = color

    