from unittest import result


class Matrix:
    '''Representa a una matriz con columnas y filas'''
    def __init__(self,*rows):
        self.checkRowLength(rows)
        self.rows = rows
        self.num_rows = len(rows)
        self.num_columns = len(rows[0])
    
    def __add__(self,anotherMatrix):
        if self.order() != anotherMatrix.order():
            raise ValueError('Las matrices deben tener el mismo order')
        result = []
        for i in range (self.num_rows):
            row = []
            for j in range(self.num_columns):
                sum_values = self.rows[i][j] + anotherMatrix.get_value(i,j)
                row.append(sum_values)
            result.append(row)
        return Matrix(result)
    
    def __mul__(self,anotherValue):
        if isinstance(anotherValue,Matrix):
            return self.multiplyByMatrix(anotherValue)
        elif isinstance(anotherValue,float):
            return self.multiplyByNumber(anotherValue)
        else:
            raise ValueError('Solo se aceptan matrices o numeros reales')
    
    def __eq__(self, anotherMatrix):
        return self.rows == anotherMatrix.rows

    def checkRowLength(self,rows):
        num_columns = len(rows[0])
        for row in rows:
            if len(row) != num_columns:
                raise ValueError('No es una matriz')

    def multiplyByNumber(self,number):
        '''Multiplica una matriz por un escalar
        number: numero real(float)
        resultado: otra Matriz
        '''
        result = []
        for i in range (self.num_rows):
            result.append([])
            for j in range(self.num_columns):
                result[i].append(self.rows[i][j] * number) 
        return Matrix(result)

    def multiplyByMatrix(self, anotherMatrix):
        '''Multiplica dos matrices 
        anotherMatrix: Segunda Matrix
        resultado: una matriz
        '''
        if self.num_columns != anotherMatrix.num_rows:
            raise ValueError('Las matrices no son compatibles porque su numero de filas y columnas')
        result = []
        for i in range (self.num_rows):
            result.append([])
            for j in range(anotherMatrix.num_columns):
                total = 0
                for r in range(self.num_columns):
                    total += self.rows[i][r] * anotherMatrix.get_value(r,j)
                result[i].append(total)
        return Matrix(result)

    def get_value(self,i,j):
        return self.rows[i][j]
    
    def __str__(self):
        matrix_str = ''
        for row in self.rows:
            for number in row:
                matrix_str += '\t' + str(number)
            matrix_str += '\n'
        return matrix_str
    
    def order(self):
        '''Calcula el orden de las matrices'''
        return self.num_rows, self.num_columns
    
    def transposed(self):
        result = []
        for i in range(self.num_columns):
            row_result = []
            #Recorro las filas
            for j in range (self.num_rows):
                row_result.append(self.rows[j][i])
            result.append(row_result)
        return Matrix(result)
