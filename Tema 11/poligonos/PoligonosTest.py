from unittest import result
from Poligonos import RegularPolygon
import unittest

class PoligonoTest(unittest.TestCase):
    def test_constructor_worksOK(self):
        # Given / When
        mypolygon = RegularPolygon(4,4)
        # Then
        self.assertIsNotNone(mypolygon)
        self.assertIsInstance(mypolygon,RegularPolygon)
        self.assertEqual(mypolygon.sideLenght,4)
        self.assertEqual(mypolygon.sideNum,4)
    
    # def test_constructor_FloatLenSideOK(self):
    #     # Given / When
    #     mypolygon = RegularPolygon(4,4.5)
    #     # Then
    #     self.assertIsNotNone(mypolygon)
    #     self.assertIsInstance(mypolygon,RegularPolygon)
    #     self.assertEqual(mypolygon.sideLenght,4.5)
    #     self.assertEqual(mypolygon.sideNum,4)
    
    # @unittest.expectedFailure
    # def test_constructor_NumberSidesFail(self):
    #     # Given / When
    #     mypolygon = RegularPolygon(2,5)

    @unittest.expectedFailure
    def test_constructor_failure(self):
        # Given / When
        mypolygon = RegularPolygon(True,'hola')

    @unittest.expectedFailure
    def test_constructor_NegativeLengthSide(self):
        # Given / When
        mypolygon = RegularPolygon(2,-5)
    
    def test_str(self):
        # Given
        number_sides = 3
        len_sides = 7
        my_polygon = RegularPolygon(len_sides,number_sides)
        expected_text = f'Polígono con {len_sides} lados y {number_sides} de longitud cada lado'
        # When
        result = str(my_polygon)
        # Then
        self.assertEqual(result,expected_text)

######

    def test_perimeterSquare(self):
        # Given
        num_sides = 4
        len_sides = 4
        expected_result = 16
        mypolygon = RegularPolygon(num_sides,len_sides)
        # When
        result = mypolygon.calculatePerimeter()
        # Then
        self.assertIsNotNone(result)
        self.assertGreater(result,0)
        self.assertEqual(result,expected_result)
    
    def test_perimeterTriangle(self):
        # Given
        num_sides = 3
        len_sides = 10.5
        expected_result = 31.5
        mypolygon = RegularPolygon(num_sides,len_sides)
        # When
        result = mypolygon.calculatePerimeter()
        # Then
        self.assertIsNotNone(result)
        self.assertGreater(result,0)
        self.assertEqual(result,expected_result)
    
    # def test_Apothem_Square(self):
    #     # Given
    #     mypolygon = RegularPolygon(2,4)
    #     # When
    #     result = mypolygon.calculateApothem()
    #     # Then
    #     self.assertAlmostEqual(result,3)

    # def test_Apothem_Triangle(self):
    #     # Given
    #     mypolygon = RegularPolygon(3,2)
    #     # When
    #     result = mypolygon.calculateApothem()
    #     # Then
    #     self.assertAlmostEqual(result,0.58, 2)

    # def test_Apothem_Decagon(self):
    #     # Given
    #     mypolygon = RegularPolygon(10,28)
    #     # When
    #     result = mypolygon.calculateApothem()
    #     # Then
    #     self.assertAlmostEqual(result,43.08757, 5)

    # def test_area_Square(self):
    #     # Given
    #     mypolygon = RegularPolygon(4,2)
    #     # When
    #     result = mypolygon.calculateArea()
    #     # Then
    #     self.assertAlmostEqual(result,4)
    
    # def test_area_Triangle(self):
    #     # Given
    #     mypolygon = RegularPolygon(3,4)
    #     # When
    #     result = mypolygon.calculateArea()
    #     # Then
    #     self.assertAlmostEqual(result,6.928)
    
    # def test_area_Hexagon(self):
    #     # Given
    #     mypolygon = RegularPolygon(6,7.5)
    #     # When
    #     result = mypolygon.calculateArea()
    #     # Then
    #     self.assertAlmostEqual(result,146.14,2)
######

    def test_colorPolygon(self):
        # Given
        num_sides = 4
        len_sides = 5
        # When
        mypolygon = RegularPolygon(len_sides,num_sides)
        # Then
        self.assertNotEqual(mypolygon.mycolor,'white')

    def test_ParamcolorPolygon(self):
        # Given
        num_sides = 4
        len_sides = 5
        mycolor = 'red'
        # When
        mypolygon = RegularPolygon(len_sides,num_sides,mycolor)
        # Then
        self.assertNotEqual(mypolygon.mycolor,'white')
        self.assertEqual(mypolygon.mycolor,mycolor)

######

    def test_SameValuesPolygons(self):
        # Given
        num_sides = 4
        len_sides = 5
        mypolygon1 = RegularPolygon(len_sides,num_sides)
        mypolygon2 = RegularPolygon(len_sides,num_sides)
        # When
        result = mypolygon1 == mypolygon2
        # Then
        self.assertTrue(result)
    
    def test_DifferentValuesPolygons(self):
        # Given
        num_sides1 = 7
        num_sides2 = 5
        len_sides = 6
        mypolygon1 = RegularPolygon(len_sides,num_sides1)
        mypolygon2 = RegularPolygon(len_sides,num_sides2)
        # When
        # Then
        self.assertNotEquals(mypolygon1, mypolygon2)
    
    def test_GreaterSameValuesPolygons(self):
        # Given
        num_sides1 = 4
        len_sides1 = 5
        mypolygon1 = RegularPolygon(len_sides1,num_sides1)
        mypolygon2 = RegularPolygon(len_sides1,num_sides1)
        # When
        # Then
        self.assertFalse(mypolygon1 > mypolygon2)
        self.assertFalse(mypolygon2 > mypolygon1)
    
    def test_Greater_DifferentValuesPolygons(self):
        # Given
        num_sides1 = 8
        num_sides2 = 4
        len_sides1 = 7
        mypolygon1 = RegularPolygon(len_sides1,num_sides1)
        mypolygon2 = RegularPolygon(len_sides1,num_sides2)
        # When
        # Then
        self.assertGreater(mypolygon1, mypolygon2)
        self.assertFalse(mypolygon2 > mypolygon1)
    
    def test_Greater_TriangleBiggerThanSquare(self):
        # Given
        num_sides1 = 4
        num_sides2 = 3
        len_sides1 = 2
        len_sides2 = 20
        mypolygon1 = RegularPolygon(len_sides1,num_sides1)
        mypolygon2 = RegularPolygon(len_sides2,num_sides2)
        # When
        # Then
        self.assertGreater(mypolygon2, mypolygon1)
        self.assertFalse(mypolygon1 > mypolygon2)


if __name__ == '__main__':
    unittest.main()