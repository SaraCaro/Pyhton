from matrices import Matrix
import unittest

class MatrixTest(unittest.TestCase):
    def test_constructor_OneRowOK(self):
        # Given
        row = [1,3]
        # When
        myMatrix = Matrix(row)
        # Then
        self.assertIsNotNone(myMatrix)
        self.assertIsInstance(myMatrix,Matrix)
        self.assertEqual(myMatrix.num_rows,1)
        self.assertEqual(myMatrix.num_columns,len(row))
        self.assertEqual(myMatrix.rows, (row,))
    
    def test_constructor_SeveralRowsOK(self):
        # Given
        rows = ([1,3,6],[6,7,8],)
        # When
        myMatrix = Matrix(*rows)
        # Then
        self.assertIsNotNone(myMatrix)
        self.assertIsInstance(myMatrix,Matrix)
        self.assertEqual(myMatrix.num_rows,len(rows))
        self.assertEqual(myMatrix.num_columns,len(rows[0]))
        self.assertEqual(myMatrix.rows, rows)
    
    @unittest.expectedFailure
    def test_constructor_SeveralRows_DifferentLength_Fail(self):
        # Given
        rows = ([1,3,6],[6,7],)
        # When 
        myMatrix = Matrix(*rows)
    
    def test_constructor_ThreeDimensionsOK(self):
        # Given
        rows = (
            [
                [4,5,6],
                [3,8,9],
                [9,4,3]
            ],
            [
                [7,6,9],
                [4,2,4],
                [1,7,8]
            ],
        )

        # When
        myMatrix = Matrix(*rows)
        # Then
        self.assertIsNotNone(myMatrix)
        self.assertIsInstance(myMatrix,Matrix)
        self.assertEqual(myMatrix.num_rows,len(rows))
        self.assertEqual(myMatrix.num_columns,len(rows[0]))
        self.assertEqual(myMatrix.rows, rows)
    
    def test_getValues_OK(self):
        # Given
        rows = ([1,3,6],[6,7,8],)
        myMatrix = Matrix(*rows)
        expected_value = 6
        # When
        result = myMatrix.get_value(0,2)
        # Then
        self.assertEqual(expected_value, result)
    
    def test_order_OK(self):
        # Given
        rows = ([1,3,6],[6,7,8],)
        myMatrix = Matrix(*rows)
        expected_value = (2,3)
        # When
        result = myMatrix.order()
        # Then
        self.assertEqual(expected_value, result)

    def test_str_OK(self):
        # Given
        rows = ([1,3,6],[6,7,8],)
        myMatrix = Matrix(*rows)
        expected_value = f'\t1\t3\t6\n\t6\t7\t8\n'
        # When
        result = str(myMatrix)
        # Then
        self.assertEqual(expected_value, result)
    
    # def test_transposed_OneRow_OK(self):
    #     # Given
    #     row = [1,3]
    #     myMatrix = Matrix(row)
    #     expected_value = Matrix([1],[3])
    #     # When
    #     result = myMatrix.transposed()
    #     # Then
    #     self.assertEqual(expected_value,result)

    # def test_transposed_OneColumn_OK(self):
    #     # Given
    #     row = ([1],[3],)
    #     myMatrix = Matrix(*row)
    #     expected_value = Matrix([1,3])
    #     # When
    #     result = myMatrix.transposed()
    #     # Then
    #     self.assertEqual(expected_value,result)
    
    # def test_transposed_TwoRows_ThreeColumns_OK(self):
    #     # Given
    #     rows = ([1,3,6],[6,7,8],)
    #     myMatrix = Matrix(*rows)
    #     expected_value = Matrix([1,6],[3,7],[6,8])
    #     # When
    #     result = myMatrix.transposed()
    #     # Then
    #     self.assertEqual(expected_value,result) 
    
    def test_add_OneRowOK(self):
        # Given
        first_matrix = Matrix([4])
        second_matrix = Matrix([5])
        expected_value = Matrix([9])
        # When
        result = first_matrix + second_matrix
        # Then
        self.assertEqual(expected_value,result)

if __name__ == '__main__':
    unittest.main()