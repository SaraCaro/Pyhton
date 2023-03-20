import math

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'
    
    def quadrant(self):
        if self.x == 0 and self.y != 0:
            print('Esta situado en el eje y')
        elif self.x != 0 and self.y == 0:
            print('Esta situado en el eje X')
        elif self.x == 0 and self.y == 0:
            print('Esta situado sobre el origen')
    
    def calculateDistance(self,anotherPoint):
        return math.sqrt(
            (anotherPoint.x - self.x)**2 + (anotherPoint.y - self.y)**2
        )

class myVector:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
    
    def sumVector(self,anotherVector):
        p1sumx = self.p1.x + anotherVector.p1.x
        p1sumy = self.p1.y + anotherVector.p1.y
        p2sumx = self.p2.x + anotherVector.p2.x
        p2sumy = self.p2.y + anotherVector.p2.y
        return(myVector(Point(p1sumx,p1sumy),Point(p2sumx,p2sumy)))

    def sumEscalar(self,escalar):
        p1 = Point(escalar*self.p1.x,escalar*self.p1.y)
        p2 = Point(escalar*self.p2.x,escalar*self.p2.y)
        return myVector(p1,p2)
    
    def distanceVector(self):
        return self.p1.calculateDistance(self.p2)
    
    def vectorial(self,anotherVector):
        p1sumx = self.p1.x * anotherVector.p1.x
        p1sumy = self.p1.y * anotherVector.p1.y
        p2sumx = self.p2.x * anotherVector.p2.x
        p2sumy = self.p2.y * anotherVector.p2.y
        return(myVector(Point(p1sumx,p1sumy),Point(p2sumx,p2sumy)))

    def escalarProduct(self,anotherVector):
        p1sumx = self.p1.x * anotherVector.p1.x
        p1sumy = self.p1.y * anotherVector.p1.y
        p2sumx = self.p2.x * anotherVector.p2.x
        p2sumy = self.p2.y * anotherVector.p2.y
        return p1sumx+p1sumy+p2sumx+p2sumy


punto = Point(3,7)
punto2 = Point(1,10)
print(punto2)
print(punto2.calculateDistance(punto))

vector1 = myVector(Point(3,7),Point(6,9))
vector2 = myVector(Point(1,10),Point(2,8))
print(vector1)
print(vector1.escalarProduct(vector2))