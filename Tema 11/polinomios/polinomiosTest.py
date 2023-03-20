import unittest,random
from unittest import expectedFailure, result
from polinomios import Polynomial


class PolynomialTest(unittest.TestCase):
    def test_constructor_OneParamOk(self):
        # Given
        num1 = 1
        # When
        myPolinomio = Polynomial(num1)
        # Then
        self.assertIsNotNone(myPolinomio)
        self.assertIsInstance(myPolinomio,Polynomial)
        self.assertEqual(len(myPolinomio.coeficients), 1)
        self.assertEqual(num1, myPolinomio.coeficients[0])

    def test_constructor_SeveralParam_Ok(self):
        # Given
        myTuples = (1,3,5,9,12)
        # When
        myPolinomio = Polynomial(*myTuples)
        # Then
        self.assertIsNotNone(myPolinomio)
        self.assertIsInstance(myPolinomio,Polynomial)
        self.assertEqual(len(myPolinomio.coeficients), len(myTuples))
        self.assertEqual(myTuples, myPolinomio.coeficients)

    def test_constructor_ManyRandomParam_Ok(self):
        # Given
        num_param = 200
        myList = []
        for i in range(num_param):
            myList.append(random.randint(0,num_param))

        # When
        myPolinomio = Polynomial(*myList)
        # Then
        self.assertIsNotNone(myPolinomio)
        self.assertIsInstance(myPolinomio,Polynomial)
        self.assertEqual(len(myPolinomio.coeficients), len(myList))
        self.assertEqual(tuple(myList), myPolinomio.coeficients)
    
    def test_str_OneParam(self):
        # Given
        num1 = 1
        myPolinomio = Polynomial(num1)
        expected_text = f'{num1}'
        # When
        result = str(myPolinomio)
        # Then
        self.assertEqual(result,expected_text)
    
    def test_str_SeveralParam(self):
        # Given
        myTuple = (1,2,5,)
        myPolinomio = Polynomial(*myTuple)
        expected_text = f'{myTuple[0]}+{myTuple[1]}x**1+{myTuple[2]}x**2'
        # When
        result = str(myPolinomio)
        # Then
        self.assertEqual(result,expected_text)

    def test_str_SeveralParamWithCero(self):
        # Given
        myTuple = (1,0,5,)
        myPolinomio = Polynomial(*myTuple)
        expected_text = f'{myTuple[0]}+{myTuple[2]}x**2'
        # When
        result = str(myPolinomio)
        # Then
        self.assertEqual(result,expected_text)
    
    def test_str_SeveralStartWithZero(self):
        # Given
        myTuple = (0,2,5,)
        myPolinomio = Polynomial(*myTuple)
        expected_text = f'+{myTuple[1]}x**1+{myTuple[2]}x**2'
        # When
        result = str(myPolinomio)
        # Then
        self.assertEqual(result,expected_text)
    
    def test_str_SeveralWithFinalZero(self):
        # Given
        myTuple = (4,3,0,0,)
        myPolinomio = Polynomial(*myTuple)
        expected_text = f'{myTuple[0]}+{myTuple[1]}x**1'
        # When
        result = str(myPolinomio)
        # Then
        self.assertEqual(result,expected_text)
    
    def test_grade_OneParamOK(self):
        # Given
        num1 = 1
        myPolinomio = Polynomial(num1)
        expected_text = 0
        # When
        result = myPolinomio.grado()
        # Then
        self.assertEqual(result,expected_text)
    
    def test_grade_SeveralParam_Ok(self):
        # Given
        myTuples = (1,3,5,9,12)
        myPolinomio = Polynomial(*myTuples)
        expected_text = len(myTuples)-1
         # When
        result = myPolinomio.grado()
        # Then
        self.assertEqual(result,expected_text)
    
    def test_grade_SeveralParamWithZeroInBetween_Ok(self):
        # Given
        myTuples = (1,3,0,9,12)
        myPolinomio = Polynomial(*myTuples)
        expected_text = len(myTuples)-1
         # When
        result = myPolinomio.grado()
        # Then
        self.assertEqual(result,expected_text)
    
    def test_grade_SeveralParamWithZeroAtStart_Ok(self):
        # Given
        myTuples = (0,3,-5,9,-12)
        myPolinomio = Polynomial(*myTuples)
        expected_text = len(myTuples)-1
         # When
        result = myPolinomio.grado()
        # Then
        self.assertEqual(result,expected_text)
    
    def test_grade_SeveralParamWithFinalZero_Ok(self):
        # Given
        myTuples = (1,3,-5,9,0,0)
        myPolinomio = Polynomial(*myTuples)
        expected_text = 3
         # When
        result = myPolinomio.grado()
        # Then
        self.assertEqual(result,expected_text)
    
    # def test_eq(self):
    #     # Given
    #     my_pol1 = Polynomial(3,6,1)
    #     my_pol2 = Polynomial(7,1,2,0)
    #     # When/Then
    #     self.assertEqual(my_pol1,my_pol2)

    # def test_suma_SameGrade(self):
    #     # Given
    #     my_pol1 = Polynomial(3,6,1)
    #     my_pol2 = Polynomial(7,1,2)
    #     expected_text = Polynomial(10,7,3)
    #     # When
    #     result = my_pol1 + my_pol2
    #     # Then
    #     self.assertEqual(result, expected_text)

    # def test_suma_DifferentGrade(self):
    #     # Given
    #     my_pol1 = Polynomial(3,6,1)
    #     my_pol2 = Polynomial(7,1,2,7)
    #     expected_text = Polynomial(10,7,3,7)
    #     # When
    #     result = my_pol1 + my_pol2
    #     # Then
    #     self.assertEqual(result, expected_text)

    # def test_suma_SameGradeWithZeros_NegativeValues(self):
    #     # Given
    #     my_pol1 = Polynomial(-3,6,-1)
    #     my_pol2 = Polynomial(7,0,-2)
    #     expected_text = Polynomial(4,6,-3)
    #     # When
    #     result = my_pol1 + my_pol2
    #     # Then
    #     self.assertEqual(result, expected_text)
    
    
if __name__ == '__main__':
    unittest.main()
