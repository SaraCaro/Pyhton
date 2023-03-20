import unittest

class MyTest(unittest.TestCase):
    def test(self):
        assert(True)

    def test2(self):
        assert(False)
    
    def test3(self):
        assert(7 >= 5)
    
    def test4(self):
        assert(1 == '1')

    def test5(self):
        assert(5.0 > 0)
    
    def test6(self):
        assert(5)
    
    def test7(self):
        assert(0)
    
    def test8(self):
        assert(None)
    
    def test9(self):
        assert('')
    
    def test10(self):
        assert(True)
        assert(diez > 0)
        assert(-1 >= 10)

if __name__ == '__main__':
    unittest.main()