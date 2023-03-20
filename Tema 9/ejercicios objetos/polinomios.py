class Polynomial:
    '''Representa un polinomio almacenando los coeficientes 
    que forman parte del mismo'''
    def __init__(self,*args):
        self.coeficients = args

    def __str__(self):
        if self.coeficients[0] != 0:
            result = str(self.coeficients[0])
        else:
            result = ''
        n = len(self.coeficients)
        for i in range (1,n):
            if self.coeficients[i] == 0:
                continue
            if i > 0:
                simbol = '+'
            else:
                simbol = ''
            result += f'{simbol} {self.coeficients[i]}x**{i}'
        return result

    #self.coeficients.reverse()
        #polinomio = []
        #potencia = 0
        #for coeficiente in self.coeficients:
        #   polinomio.append(f'{coeficiente}x{potencia}')
        #   potencia += 1
        
        #polinomio.reverse()
        #polinomio_str = ' + '.join(polinomio)
        #return polinomio_str

    def __add__(self, anotherPolynomial):
        grado_self = self.grado
        grado_anotherPoli = anotherPolynomial.grado()
        grado_min = min(grado_self,grado_anotherPoli)

        result = []
        for i in range(grado_min + 1):
            result.append(self.coeficients[i] + anotherPolynomial.coeficients[i])
        if grado_self != grado_anotherPoli:
            if grado_self == grado_min:
                result.append(anotherPolynomial.coeficients[grado_min + 1:])
            else:
                result.append(self.coeficients[grado_min + 1:])
        
        return Polynomial(*result)
        
    def __mul__(self,anotherPolynomial):
        result = []
        grado_self = self.grado
        grado_anotherPoli = anotherPolynomial.grado()
        for i in range(grado_self + grado_anotherPoli + 1):
            result.append(0)
            # recorremos el primer polinomio
        for i in range(grado_self + 1):
            if self.coeficients[i] == 0:
                continue
            # recorremos el segundo polinomio
            for j in range(grado_anotherPoli + 1):
                if anotherPolynomial.coeficients[j] == 0:
                    continue
                product = self.coeficients[i] * anotherPolynomial.coeficients[j]
                index = i + j
                result[index] += product

        return Polynomial(*result)
                
    def grado(self):
        '''Calcula el grado
        @return: numero(int)
        '''
        return len(self.coeficients) - 1
        
        
