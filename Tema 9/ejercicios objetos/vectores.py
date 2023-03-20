from puntos import Points

class myVector:
    def __init__(self,p1,p2):
        '''Representa un vector matemático definido por A y B'''
        self.p1 = p1
        self.p2 = p2
    
    def __str__(self):
        return f'({self.p1},{self.p2})'
    
    def sumVector(self,anotherVector):
        p1sumx = self.p1.x + anotherVector.p1.x
        p1sumy = self.p1.y + anotherVector.p1.y
        p2sumx = self.p2.x + anotherVector.p2.x
        p2sumy = self.p2.y + anotherVector.p2.y
        return(myVector(Points(p1sumx,p1sumy),Points(p2sumx,p2sumy)))
    

    def sumEscalar(self,escalar):
        p1 = Points(escalar*self.p1.x,escalar*self.p1.y)
        p2 = Points(escalar*self.p2.x,escalar*self.p2.y)
        return myVector(p1,p2)
    
    def distanceVector(self):
        '''Metodo que calcula la distancia del Vector
        Resultado: valor numérico(float)
        '''
        return self.p1.calculateDistance(self.p2)
    
    def vectorial(self,anotherVector):
        p1sumx = self.p1.x * anotherVector.p1.x
        p1sumy = self.p1.y * anotherVector.p1.y
        p2sumx = self.p2.x * anotherVector.p2.x
        p2sumy = self.p2.y * anotherVector.p2.y
        return(myVector(Points(p1sumx,p1sumy),Points(p2sumx,p2sumy)))

    def escalarProduct(self,anotherVector):
        p1sumx = self.p1.x * anotherVector.p1.x
        p1sumy = self.p1.y * anotherVector.p1.y
        p2sumx = self.p2.x * anotherVector.p2.x
        p2sumy = self.p2.y * anotherVector.p2.y
        return p1sumx+p1sumy+p2sumx+p2sumy



vector1 = myVector(Points(3,7),Points(6,9))
vector2 = myVector(Points(1,10),Points(2,8))
print(vector1)
print(vector1.escalarProduct(vector2))


